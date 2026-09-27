import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart';

void main() {
  runApp(const GuardWellApp());
}

class GuardWellApp extends StatelessWidget {
  const GuardWellApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'GuardWell',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.red,
        ),
        useMaterial3: true,
      ),
      home: const WelcomeScreen(),
    );
  }
}