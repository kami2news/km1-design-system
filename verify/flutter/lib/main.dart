import 'package:flutter/material.dart';
import 'km1_theme.dart';
import 'gallery.dart';

void main() => runApp(const Km1VerifyApp());

class Km1VerifyApp extends StatelessWidget {
  const Km1VerifyApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
        title: 'KM1 検証',
        theme: Km1Theme.light(),
        darkTheme: Km1Theme.dark(),
        home: const Km1Gallery(),
      );
}
