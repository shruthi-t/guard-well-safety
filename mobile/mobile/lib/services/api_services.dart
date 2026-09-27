import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:8000';

  // -------------------------
  // USER REGISTRATION
  // -------------------------
  static Future<Map<String, dynamic>> register({
    required String name,
    required String mobile,
    String? email,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/register'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'name': name,
        'mobile': mobile,
        'email': email,
        'password': password,
      }),
    );

    if (response.statusCode == 200 ||
        response.statusCode == 201) {
      return jsonDecode(response.body);
    }

    throw Exception(
      'Server error ${response.statusCode}: ${response.body}',
    );
  }

  // -------------------------
  // USER LOGIN
  // -------------------------
  static Future<Map<String, dynamic>> login({
    required String mobileOrEmail,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/login'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'mobile_or_email': mobileOrEmail,
        'password': password,
      }),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception(
      'Server error ${response.statusCode}: ${response.body}',
    );
  }
}