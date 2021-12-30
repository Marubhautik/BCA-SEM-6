import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'LocalNotifyManager.dart';

class TestNotifyscreen extends StatefulWidget {

  @override
  _TestNotifyscreenState createState() => _TestNotifyscreenState();
}

class _TestNotifyscreenState extends State<TestNotifyscreen> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    localNotifyManager.setOnNotificationReceive(onNotificationReceive);
    localNotifyManager.setOnNotificationClick(onNotificationClick);
  }

  onNotificationReceive(ReceiveNotification notification){
    print('Notification received: ${notification.id}');
  }

  onNotificationClick(payload){
    print('payload $payload');
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:Text('Local Notification'),
        centerTitle: true,
        backgroundColor: Colors.redAccent,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.only(bottomRight: Radius.elliptical(200, 500),bottomLeft: Radius.elliptical(200, 500))
        ),
      ),
      body: Center(
        child: FlatButton(
          onPressed: () async{
            await localNotifyManager.ShowNotification();
          },
          child: Text('Send Notification bhautik'),
          textColor: Colors.red,
        ),
      )
    );
  }
}
