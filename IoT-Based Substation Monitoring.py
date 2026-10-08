## IoT-Based Substation Monitoring — Simple Python Program

This beginner-level program simulates monitoring important substation parameters such as **voltage, current, temperature, and transformer oil temperature**.

```
# IoT-Based Substation Monitoring

voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
temperature = float(input("Enter Transformer Temperature (°C): "))

print("\n--- Substation Status ---")
print("Voltage =", voltage, "V")
print("Current =", current, "A")
print("Temperature =", temperature, "°C")

if temperature > 80:
    print("WARNING: High Transformer Temperature!")
elif voltage < 200:
    print("WARNING: Low Voltage!")
elif voltage > 250:
    print("WARNING: High Voltage!")
else:
    print("Substation Status: NORMAL")
```

### Example Output

```
Enter Voltage (V): 230
Enter Current (A): 50
Enter Transformer Temperature (°C): 65

--- Substation Status ---
Voltage = 230.0 V
Current = 50.0 A
Temperature = 65.0 °C
Substation Status: NORMAL
```

### With IoT-style alert

```
voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
temperature = float(input("Enter Temperature (°C): "))

print("\nSending data to IoT server...")

if temperature > 80 or voltage < 200 or voltage > 250:
    print("ALERT: Abnormal condition detected!")
else:
    print("Data sent successfully.")
    print("Substation is NORMAL.")
```

**Project name:** IoT-Based Substation Monitoring System

**Parameters monitored:**

- Voltage
- Current
- Transformer temperature
- Fault/abnormal condition
- Remote alert

This Python code is a **simulation**; a real IoT project would connect sensors such as voltage/current/temperature sensors to an **ESP32/Arduino** and send the readings to a cloud or monitoring dashboard.
