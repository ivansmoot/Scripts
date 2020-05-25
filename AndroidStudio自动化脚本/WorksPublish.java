package com.versa;

import android.content.Context;
import android.content.Intent;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.filters.LargeTest;
import androidx.test.platform.app.InstrumentationRegistry;
import static androidx.test.espresso.action.ViewActions.click;
import com.versa.ui.VersaHomeActivity;
import com.versa.ui.template.TemplateActivity;
import com.versa.ui.mine.SettingMoreActivity;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import org.junit.Test;
import org.junit.runner.RunWith;
import static androidx.test.espresso.Espresso.onView;
import static org.junit.Assert.*;
import android.support.test.uiautomator.*;
import android.util.Log;

/**
 * uiautomator的逻辑是：如果查找一个元素，会等待这个元素出现，出现了就做一次操作
 * 所以有的按钮会被点击过快，在不应该点击的时候就被点击了，导致没有效果
 * 需要进行一次等待，例如发布页，需要等待直到右上角的退出按钮可以被点击时再进行点击操作
 */

@RunWith(AndroidJUnit4.class)
@LargeTest
public class WorksPublish {
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
            // 等待加号加载出来，判断一下有没有未完成的作品提示框
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/toolbar_workspace")).waitForExists(10000);
            if(uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_content")).exists()) {
                uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tv_cancel")).click();
            }
            // 点击加号，进入模板页，没有直接启动模板页的Activity是因为这样做的话，返回键会直接返回到桌面
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/toolbar_workspace")).click();
            // 等待模板加载出来，因为不加载出来的话，没办法判断，后面不用，等着就行
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tvDesc")).waitForExists(10000);
            // 判断引导，如果有做同款按钮的话，先返回到主页，再重新进
            if(uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tvTry")).exists()){
                uiDevice.pressBack();
                uiDevice.findObject(new UiSelector().resourceId("com.versa:id/toolbar_workspace")).click();
            }
            // 点击右上角"所有图片"按钮，这里不用显式等待，因为默认就在等
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tvDesc")).click();
            // 点击第三张小狗样片
            uiDevice.findObject(new UiSelector().textContains("样片").instance(2)).click();
            // 等一下分割，通过有没有左下角的图层顺序按钮判断，有那个按钮，就代表分割好了
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/rl_first_lever_menu")).waitForExists(10000);
            // 做一个inpainting，steps越多，移动越慢
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/paster_container")).dragTo(900,500,100);
            // 点一下滤镜，这里不好判断是否inpainting结束，做了一个sleep
            Thread.sleep(3000);
            uiDevice.findObject(new UiSelector().textMatches("滤镜")).click();
            // 点叉号，马卡龙每两个操作需要间隔一定时间，否则不生效
            Thread.sleep(2000);
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/second_level_cancel")).click();
            // 点击完成按钮
            Thread.sleep(2000);
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/edit_complete_normal")).click();
            // 等待保存完成，即右上角的"退出"按钮可点
            uiDevice.findObject(new UiSelector().textContains("退出").clickable(true)).waitForExists(10000);
            // 点击发布
            uiDevice.findObject(new UiSelector().resourceId("com.versa:id/tvRight")).click();

            // 断言
            assertTrue(uiDevice.findObject(new UiSelector().textContains("发布成功")).exists());
        } catch(Exception e) {
            e.printStackTrace();
            Log.e("yifan_test","登陆时出错");
        }
    }
}
