import 'package:flutter/material.dart';
import 'TestNotifyscreen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: TestNotifyscreen(),
    );
  }
}

