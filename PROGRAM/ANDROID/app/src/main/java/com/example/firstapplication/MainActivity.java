package com.example.firstapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button btn;
    EditText edt1,edt2;
    TextView txt_welcome;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        edt1 = findViewById(R.id.m_edt1);
        edt2 = findViewById(R.id.m_edt2);
        btn =findViewById(R.id.m_btn);
        txt_welcome = findViewById(R.id.m_txt_w)
    }
}