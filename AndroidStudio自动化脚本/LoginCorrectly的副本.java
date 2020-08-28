package com.versa;

import android.content.Context;
import android.content.Intent;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.filters.LargeTest;
import androidx.test.platform.app.InstrumentationRegistry;
import static androidx.test.espresso.action.ViewActions.click;
import com.versa.ui.VersaHomeActivity;
import com.versa.ui.mine.SettingMoreActivity;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import org.junit.Test;
import org.junit.runner.RunWith;
import static androidx.test.espresso.Espresso.onView;
import static org.junit.Assert.*;
import android.support.test.uiautomator.*;
import android.util.Log;

/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */

@RunWith(AndroidJUnit4.class)
@LargeTest
public class LoginCorrectly {
    @Test
    public void main_logic() {
        // 建立上下文
        Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
        // 设置uiDevice，后面的操作要靠这个类
        UiDevice uiDevice = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
        // 马卡龙首页的Activity
        Intent intent = new Intent(appContext, VersaHomeActivity.class);
        // 把将要启动的Activity放在一个新栈中，否则会报错
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

        // 启动马卡龙首页
        appContext.startActivity(intent);
        try{
            // 点击右下角的"我的"按钮
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/toolbar_usercenter")).click();
            // 判断是否登陆，如果登陆了，就先退出登陆
            if(!(uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_user_name")).getText()).equals("欢迎来到马卡龙")){
                // 切换到设置页Activity
                Intent intent2 = new Intent(appContext, SettingMoreActivity.class);
                intent2.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                appContext.startActivity(intent2);
                // 点击退出登陆按钮
                uiDevice.findObject(new UiSelector().resourceId("com.versa:id/btn_exit")).click();
                // 点击确定
                uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_delete")).click();
            }
            // 点击登陆按钮
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_login")).click();
            // 点击协议框下面的确认按钮
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_confirm")).click();
            // 输入手机号
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/et_tel")).setText("178 6397 7623");
            // 点击箭头按钮
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/iv_next")).click();
            // 输入密码
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/et_input_01")).setText("miss1186285865");
            // 点击箭头按钮，这一步有时会失败，加一个线程等待
            while (uiDevice.findObject(new UiSelector().resourceId("com.versa:id/iv_next")).isEnabled()) {
                uiDevice.findObject(new UiSelector().resourceId("com.versa:id/iv_next")).click();
            }
            // 断言已登陆，即用户名不是"欢迎来到马卡龙"
            assertNotEquals("欢迎来到马卡龙",
                    uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_user_name")).getText());
        } catch(Exception e) {
            e.printStackTrace();
            Log.e("yifan_test","登陆时出错");
        }
    }
}
