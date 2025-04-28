import streamlit as st


def main():
    st.title("Download ADT android development tool kit")
    st.write("http://bit.ly/35GUYzF")

    st.title("layout")
    st.write("xml code in activity_main")
    st.code("""
    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp"
    tools:context=".MainActivity" >

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_centerInParent="true">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Student Information"
            android:textAppearance="?android:attr/textAppearanceLarge"
            android:textStyle="bold"
            android:layout_gravity="center" />

        <EditText
            android:id="@+id/editTextName"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Name" />

        <EditText
            android:id="@+id/editTextDno"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter D.NO" />

        <EditText
            android:id="@+id/editTextDept"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Department" />

        <EditText
            android:id="@+id/editTextContact"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Enter Contact Number" />

        <Button
            android:id="@+id/buttonOpenActivity2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="OK"
            android:layout_gravity="center"
            android:layout_marginTop="20dp" />

    </LinearLayout>

</RelativeLayout>""")
    st.write("activity2.xml")
    st.code("""
    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="20dp" >
    
    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:layout_marginTop="32dp"
        android:paddingBottom="10dp"
        android:text="STUDENT INFORMATION"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:textStyle="bold" />

    <TextView
        android:id="@+id/textViewDno"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/textViewName"
        android:layout_below="@+id/textViewName"
        android:text="D.NO:" />

    <TextView
        android:id="@+id/textViewContact"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewDept"
        android:layout_below="@+id/textViewDno"
        android:text="ContactNO:" />

    <TextView
        android:id="@+id/textViewName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignRight="@+id/textViewContact"
        android:layout_below="@+id/textView1"
        android:layout_marginTop="18dp"
        android:text="Name:" />

    <TextView
        android:id="@+id/textViewDept"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/textViewContact"
        android:text="Department:" />

</RelativeLayout>""")
    st.write("activity1.java")
    st.code("""
    package com.example.layout;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class activity1 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText editTextName = (EditText) findViewById(R.id.editTextName);
        final EditText editTextDno = (EditText) findViewById(R.id.editTextDno);
        final EditText editTextDept = (EditText) findViewById(R.id.editTextDept);
        final EditText editTextContact = (EditText) findViewById(R.id.editTextContact);
        Button buttonOpenActivity2 = (Button) findViewById(R.id.buttonOpenActivity2);

        buttonOpenActivity2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = editTextName.getText().toString();
                String dno = editTextDno.getText().toString();
                String department = editTextDept.getText().toString();
                String contact = editTextContact.getText().toString();

                Intent intent = new Intent(activity1.this, activity2.class);
                intent.putExtra("NAME", name);
                intent.putExtra("DNO", dno);
                intent.putExtra("DEPARTMENT", department);
                intent.putExtra("CONTACT", contact);
                startActivity(intent);
            }
        });
    }
}""")
    st.write("activity2.java")
    st.code("""
    package com.example.layout;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class activity2 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity2);

        TextView textViewName = (TextView) findViewById(R.id.textViewName);
        TextView textViewDno = (TextView) findViewById(R.id.textViewDno);
        TextView textViewDept = (TextView) findViewById(R.id.textViewDept);
        TextView textViewContact = (TextView) findViewById(R.id.textViewContact);

        String name = getIntent().getStringExtra("NAME");
        String dno = getIntent().getStringExtra("DNO");
        String department = getIntent().getStringExtra("DEPARTMENT");
        String contact = getIntent().getStringExtra("CONTACT");

        textViewName.setText("Name:" + name);
        textViewDno.setText("D.NO:" + dno);
        textViewDept.setText("Department:" + department);
        textViewContact.setText("ContactNO:" + contact);
    }
}""")
    st.write("androidmanifist.xml")
    st.code("""
    <?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.layout"
    android:versionCode="1"
    android:versionName="1.0" >

    <uses-sdk
        android:minSdkVersion="8"
        android:targetSdkVersion="18" />

    <application
        android:allowBackup="true"
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme" >
        <activity 
            android:name=".activity1"
            
            android:label="@string/app_name" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity android:name="com.example.layout.activity2" />
    </application>

</manifest>""")




    st.title("Calculator")
    st.write("xml code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/editText11"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter first number"
        android:inputType="number" />

    <EditText
        android:id="@+id/editText22"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter second number"
        android:inputType="number" />

    <Button
        android:id="@+id/addButtonn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Add" />

    <Button
        android:id="@+id/button1"
        android:layout_width="282dp"
        android:layout_height="wrap_content"
        android:text="sub" />

    <EditText
        android:id="@+id/editText33"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:ems="10"
        android:focusable="false"
        android:hint="Result" >

        <requestFocus />
    </EditText>

</LinearLayout>""")

    st.write("mainactivity java code")
    st.code("""
package com.example.calculator;

import android.app.Activity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {

    private EditText editText1, editText2, editText3;
    private Button addButton, subbutton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        editText1 = (EditText) findViewById(R.id.editText11);
        editText2 = (EditText) findViewById(R.id.editText22);
        editText3 = (EditText) findViewById(R.id.editText33);
        addButton = (Button) findViewById(R.id.addButtonn);
        subbutton = (Button) findViewById(R.id.button1);

        // Set the button's onClickListener
        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculateSum();
            }
        });
        subbutton.setOnClickListener(new View.OnClickListener(){
        	@Override
        	public void onClick(View v){
        		calculateSub();
        	}
        });
    }

    private void calculateSum() {
        // Get the input values as strings
        String input1 = editText1.getText().toString();
        String input2 = editText2.getText().toString();

        

        // Parse the inputs to integers
        
         int number1 = Integer.parseInt(input1);
         int number2 = Integer.parseInt(input2);

            // Calculate the sum
         int sum = number1 + number2;

            // Display the result in editText3
         editText3.setText(String.valueOf(sum));
        
    }
    
    
    private void calculateSub() {
        // Get the input values as strings
        String input1 = editText1.getText().toString();
        String input2 = editText2.getText().toString();

        

        // Parse the inputs to integers
        
         int number1 = Integer.parseInt(input1);
         int number2 = Integer.parseInt(input2);

            // Calculate the sum
         int sum = number1 - number2;

            // Display the result in editText3
         editText3.setText(String.valueOf(sum));
        
    }
}
""")


    st.title("Business calculator")
    st.write("XML code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/costPrice"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Cost Price"
        android:inputType="numberDecimal" />

    <EditText
        android:id="@+id/sellingPrice"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Selling Price"
        android:inputType="numberDecimal" />

    <Button
        android:id="@+id/btnProfit"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Calculate Profit" />

    <Button
        android:id="@+id/btnLoss"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Calculate Loss" />

    <TextView
        android:id="@+id/result"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Result:"
        android:textSize="16sp"
        android:paddingTop="10dp" />
</LinearLayout>
""")

    st.write("mainActivity java code")

    st.code("""
package com.example.businesscalculator;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        final EditText costPrice = (EditText) findViewById(R.id.costPrice);
        final EditText sellingPrice = (EditText) findViewById(R.id.sellingPrice);
        final TextView result = (TextView) findViewById(R.id.result);
        Button btnProfit = (Button) findViewById(R.id.btnProfit);
        Button btnLoss = (Button) findViewById(R.id.btnLoss);

        // Handle Calculate Profit Button
        btnProfit.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("NewApi") @Override
            public void onClick(View v) {
                String cpText = costPrice.getText().toString().trim();
                String spText = sellingPrice.getText().toString().trim();

   

                try {
                    double cp = Double.parseDouble(cpText);
                    double sp = Double.parseDouble(spText);

                    if (sp > cp) {
                        result.setText("Profit: " + (sp - cp));
                    } else {
                        result.setText("No Profit.");
                    }
                } catch (NumberFormatException e) {
                    result.setText("Invalid input. Please enter numeric values.");
                }
            }
        });

        // Handle Calculate Loss Button
        btnLoss.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String cpText = costPrice.getText().toString().trim();
                String spText = sellingPrice.getText().toString().trim();

               

                try {
                    double cp = Double.parseDouble(cpText);
                    double sp = Double.parseDouble(spText);

                    if (cp > sp) {
                        result.setText("Loss: " + (cp - sp));
                    } else {
                        result.setText("No Loss.");
                    }
                } catch (NumberFormatException e) {
                    result.setText("Invalid input. Please enter numeric values.");
                }
            }
        });
    }
}
""")


    st.title("bouncing ball")
    st.write("Xml code")
    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:orientation="vertical" >

    <Button
        android:id="@+id/bounceBallButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:text="Bounce Ball" />

    <ImageView
        android:id="@+id/bounceBallImage"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/bounceBallButton"
        android:layout_centerHorizontal="true"
        android:background="@drawable/ball_shape" />

</RelativeLayout>
""")



    st.write("Xml code in ball image the file located in under drawable folder file name like(ball_shape.xml)")


    st.code("""
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval" >

    <solid android:color="#8c0000" />

    <stroke
        android:width="2dp"
        android:color="#fff" />
    
    <size
        android:height="80dp"
        android:width="80dp" />

</shape>
""")




    st.write("mainActivity java code")

    st.code("""
package com.example.bounc;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.animation.Animation;
import android.view.animation.BounceInterpolator;
import android.view.animation.TranslateAnimation;
import android.view.animation.Animation.AnimationListener;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends Activity {

    private static final String TAG = "AnimationStarter";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button bounceBallButton = (Button) findViewById(R.id.bounceBallButton);
        final ImageView bounceBallImage = (ImageView) findViewById(R.id.bounceBallImage);

        bounceBallButton.setOnClickListener(new OnClickListener() {

            @Override
            public void onClick(View v) {
                bounceBallImage.clearAnimation();
                TranslateAnimation transAnim = new TranslateAnimation(0, 0, 0,
                        getDisplayHeight()/2);
                transAnim.setStartOffset(500);
                transAnim.setDuration(3000);
                transAnim.setFillAfter(true);
                transAnim.setInterpolator(new BounceInterpolator());
                transAnim.setAnimationListener(new AnimationListener() {

                    @Override
                    public void onAnimationStart(Animation animation) {
                        Log.i(TAG, "Starting button dropdown animation");

                    }

                    @Override
                    public void onAnimationRepeat(Animation animation) {
                        // TODO Auto-generated method stub

                    }

                    @Override
                    public void onAnimationEnd(Animation animation) {
                        Log.i(TAG,
                                "Ending button dropdown animation. Clearing animation and setting layout");
                        bounceBallImage.clearAnimation();
                        final int left = bounceBallImage.getLeft();
                        final int top = bounceBallImage.getTop();
                        final int right = bounceBallImage.getRight();
                        final int bottom = bounceBallImage.getBottom();
                        bounceBallImage.layout(left, top, right, bottom);

                    }
                });
                bounceBallImage.startAnimation(transAnim);
            }
        });

    }

    private int getDisplayHeight() {
        return this.getResources().getDisplayMetrics().heightPixels;
    }
}
""")

    st.markdown("""<center><h1 style="color:red;">color bg change</h1></center>""",unsafe_allow_html=True)
    
    st.write("Xml code")
    st.code("""<?xml version="1.0" en
