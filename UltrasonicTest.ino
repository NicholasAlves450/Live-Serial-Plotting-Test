const int trigPin = 5; // Replace with a suitable digital pin
const int echoPin = 18; // Replace with a suitable digital pin

float duration, distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Send a 10us pulse to trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the echo time using pulseIn
  duration = pulseIn(echoPin, HIGH, 30000); // 30ms timeout for echo
  
  if (duration > 0) {
    distance = (duration * 0.0343) / 2; // Calculate distance in cm

    Serial.println(distance);

  } else {
    Serial.println(0);
  }

  delay(50);
}
