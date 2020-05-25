### 一些平时用的脚本
### 安卓自动化脚本要放在
app/src/androidTest/java/com.versa目录下<br/>
build.gradle的dependencies里添加:<br/>
testImplementation 'junit:junit:4.12'
androidTestImplementation 'androidx.test.ext:junit:1.1.1'
androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
androidTestImplementation 'androidx.test:runner:1.2.0'
androidTestImplementation 'androidx.test:rules:1.2.0'
androidTestImplementation 'com.android.support.test.uiautomator:uiautomator-v18:2.1.3'
<br/>
defaultConfig里添加:<br/>
testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"