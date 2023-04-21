import 'dart:io';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'home_screen.dart';
import 'profile_screen.dart';



List<CameraDescription> cameras = [];

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  cameras = await availableCameras();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.lightBlue,
      ),
      home: BaseScreen(),
    );
  }
}

class BaseScreen extends StatefulWidget {
  @override
  _BaseScreenState createState() => _BaseScreenState();
}

class _BaseScreenState extends State<BaseScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [HomeScreen(), CameraPage(), ProfileScreen()];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.videocam),
            label: 'Record',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
        currentIndex: _currentIndex,
        selectedItemColor: Colors.blue,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
      ),
    );
  }
}



class CameraPage extends StatefulWidget {
  @override
  _CameraPageState createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  late CameraController _controller;
  int _countdownSeconds = 10;
  bool _recording = false;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      cameras[0],
      ResolutionPreset.medium,
    );
    _controller.initialize().then((_) {
      if (!mounted) {
        return;
      }
      setState(() {});
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!_controller.value.isInitialized) {
      return Container();
    }
    return Center(
      child: Stack(
        alignment: Alignment.center,
        children: [
          ElevatedButton(
            onPressed: _recording ? null : _startRecording,
            child: Text('Record Video'),
          ),
          if (_recording)
            Text(
              '$_countdownSeconds',
              style: TextStyle(
                fontSize: 48.0,
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
        ],
      ),
    );
  }

  void _startRecording() async {
    try {
      setState(() {
        _recording = true;
      });
      await _controller.setFlashMode(FlashMode.torch);
      await _controller.setExposureOffset(-2.0);
      await _controller.startVideoRecording();
      await _startCountdown();
      final xFile = await _controller.stopVideoRecording();
      await _controller.setFlashMode(FlashMode.off);
      _showCompletedMessage(context);
      await _uploadVideo(xFile.path);
    } catch (e) {
      print('Failed to record video: $e');
    } finally {
      setState(() {
        _recording = false;
        _countdownSeconds = 10;
      });
    }
  }

  Future<void> _startCountdown() async {
    for (int i = 0; i < 10; i++) {
      await Future.delayed(const Duration(seconds: 1));
      setState(() {
        _countdownSeconds--;
      });
    }
  }

  void _showCompletedMessage(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) => AlertDialog(
        title: Text('Video Recorded'),
        content: Text('The video has been saved.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text('OK'),
          ),
        ],
      ),
    );
  }

  Future<void> _uploadVideo(String path) async {
    final file = File(path);
    final url = Uri.parse('http://10.19.9.19:5000');
    final request = http.MultipartRequest('POST', url);
    final videoStream = http.ByteStream(file.openRead());
    final videoLength = await file.length();
    final videoMultipart = http.MultipartFile(
      'video',
      videoStream,
      videoLength,
      filename: file.path.split('/').last,
    );
    request.files.add(videoMultipart);
    print(file);
    final response = await request.send();
    if (response.statusCode == 200) {
      print('Video uploaded successfully.');
    } else {
      print('Failed to upload video.');
    }
  }
}
