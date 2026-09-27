import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  final String token;

  const HomeScreen({
    super.key,
    required this.token,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('GuardWell'),
        centerTitle: true,
        automaticallyImplyLeading: false,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 20),

              const Text(
                'Welcome to GuardWell',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                ),
              ),

              const SizedBox(height: 10),

              const Text(
                'Your safety is our priority',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 16,
                  color: Colors.grey,
                ),
              ),

              const SizedBox(height: 40),

              // Emergency
              SizedBox(
                height: 90,
                child: ElevatedButton(
                  onPressed: () {
                    // Emergency screen will be connected next.
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.red,
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                  child: const Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.warning_rounded,
                        size: 35,
                      ),
                      SizedBox(width: 15),
                      Text(
                        'EMERGENCY / SOS',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 20),

              // Complaint
              SizedBox(
                height: 70,
                child: ElevatedButton.icon(
                  onPressed: () {
                    // Complaint screen will be connected next.
                  },
                  icon: const Icon(Icons.report),
                  label: const Text(
                    'Complaint Registration',
                    style: TextStyle(fontSize: 17),
                  ),
                ),
              ),

              const SizedBox(height: 15),

              // Volunteer
              SizedBox(
                height: 70,
                child: ElevatedButton.icon(
                  onPressed: () {
                    // Volunteer screen will be connected next.
                  },
                  icon: const Icon(Icons.people),
                  label: const Text(
                    'Volunteer Support',
                    style: TextStyle(fontSize: 17),
                  ),
                ),
              ),

              const Spacer(),

              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text('Logout'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}