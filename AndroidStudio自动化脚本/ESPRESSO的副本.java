package com.versa;

import android.content.Context;
import android.content.Intent;
import android.support.test.uiautomator.UiDevice;

import androidx.test.espresso.NoMatchingViewException;
import androidx.test.espresso.ViewAssertion;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.filters.LargeTest;
import androidx.test.platform.app.InstrumentationRegistry;

import com.versa.ui.template.TemplateActivity;
import com.versa.ui.VersaHomeActivity;

import static android.app.Instrumentation.ActivityResult;
import static androidx.test.espresso.Espresso.onData;
import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.action.ViewActions.click;
import static androidx.test.espresso.action.ViewActions.closeSoftKeyboard;
import static androidx.test.espresso.action.ViewActions.longClick;
import static androidx.test.espresso.action.ViewActions.typeText;
import static androidx.test.espresso.assertion.ViewAssertions.matches;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.AllOf.allOf;
import static org.junit.Assert.assertEquals;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.util.Log;
import android.view.View;

import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.filters.LargeTest;

import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import androidx.test.rule.ActivityTestRule;


/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
@LargeTest
public class ESPRESSO {
    @Rule

    public ActivityTestRule<VersaHomeActivity> activityRule =
            new ActivityTestRule<>(VersaHomeActivity.class);

    @Test
    public void listGoesOverTheFold() {
        Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();

        assertEquals("com.versa", appContext.getPackageName());
        // onData(withId(R.id.toolbar_usercenter_new)).perform(click());
        onView(withId(R.id.tv_login)).perform(click());
//        onView(withId(R.id.tv_login)).perform(click());
//        onView(withId(R.id.tv_confirm)).perform(click());
    }
}