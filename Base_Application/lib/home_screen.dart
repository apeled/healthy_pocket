import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:syncfusion_flutter_charts/charts.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String _latestMeasurement = '75';
  int _averageMeasurement = 78;

  @override
  void initState() {
    super.initState();
    _getLatestMeasurement();
    _getAverageMeasurement();
  }

  Future<String> getLatestMeasurement() async {
    final response = await http.get(Uri.parse('http://10.19.9.19:5000'));

    if (response.statusCode == 200) {
      //final jsonResponse = json.decode(response.body);
      final latestMeasurement = response.body; //jsonResponse['latest_measurement'];
      return latestMeasurement;
    } else {
      throw Exception('Failed to load latest measurement data');
    }
  }

  Future<int> getAverageMeasurement() async {
    final response = await http.get(Uri.parse('https://your-backend-api-url.com/average-measurement'));

    if (response.statusCode == 200) {
      final jsonResponse = json.decode(response.body);
      final averageMeasurement = jsonResponse['average_measurement'];
      return averageMeasurement;
    } else {
      throw Exception('Failed to load average measurement data');
    }
  }

  void _getLatestMeasurement() async {
    try {
      final latestMeasurement = await getLatestMeasurement();
      setState(() {
        _latestMeasurement = latestMeasurement;
      });
    } catch (e) {
      print('Error getting latest measurement: $e');
    }
  }

  void _getAverageMeasurement() async {
    try {
      final averageMeasurement = await getAverageMeasurement();
      setState(() {
        _averageMeasurement = averageMeasurement;
      });
    } catch (e) {
      print('Error getting average measurement: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home', style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
        elevation: 0, // remove shadow
      ),
      body: Center(
        child: SingleChildScrollView( // add scroll view
          padding: EdgeInsets.symmetric(horizontal: 16, vertical: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Container(
                height: 300,
                child: SfCartesianChart(
                  // Add your chart data and configuration here
                ),
              ),
              SizedBox(height: 32),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Column(
                    children: [
                      Icon(Icons.watch_later_outlined, size: 60),
                      SizedBox(height: 16),
                      Text('Latest', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                      SizedBox(height: 8),
                      Container(
                        width: 120,
                        padding: EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(8),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.grey.withOpacity(0.5),
                              spreadRadius: 2,
                              blurRadius: 5,
                              offset: Offset(0, 2), // add offset for shadow
                            ),
                          ],
                        ),
                        child: Center(
                          child: Text('$_latestMeasurement', style: TextStyle(fontSize: 24)),
                        ),
                      ),
                    ],
                  ),
                  Column(
                    children: [
                      Icon(Icons.analytics_outlined, size: 60),
                      SizedBox(height: 16),
                      Text('Average', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                      SizedBox(height: 8),
                      Container(
                        width: 120,
                        padding: EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(8),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.grey.withOpacity(0.5),
                              spreadRadius: 2,
                              blurRadius: 5,
                              offset: Offset(0, 2), // add offset for shadow
                            ),
                          ],
                        ),
                        child: Center(
                          child: Text('$_averageMeasurement', style: TextStyle(fontSize: 24)),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }


}
