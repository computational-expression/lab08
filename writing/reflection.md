# Lab 8 Reflection

## Dictionary Organization

Describe how you organized your dictionaries in each program (use a markdown list for this answer):

- **temperature_monitor.py dictionaries:** TODO: Describe the structure of your temperature readings dictionary. What are the keys? What type of data does each location store? How does the nested dictionary structure help organize temperature and humidity data?

- **light_monitor.py dictionaries:** TODO: Describe the structure of your light readings dictionary. Explain how you used dictionary keys and values to store location information, light levels, and brightness categories.

- **buzzer_manager.py dictionaries:** TODO: Describe the structure of your alert tracking dictionary. What information does each location entry contain? How do you use boolean values and counters in your dictionary?

## Program Integration

Describe how the three programs work together in the integrated system (use a numbered markdown list for this answer):

1. TODO: Explain how main.py initializes and connects all three modules. What happens when the program starts?

2. TODO: Describe how each module operates independently. Can you use temperature_monitor without the other modules?

3. TODO: Explain how location IDs help coordinate data across the three different dictionaries.

4. TODO: Describe how the main program detects problems by calling alert checking functions from different modules.

5. TODO: Explain how the main program triggers buzzers when sensor readings exceed thresholds.

6. TODO: Describe the complete flow from sensor reading to buzzer activation for a temperature or light alert.

7. TODO: Explain what information the system summary displays and how it combines data from all three modules.

## Git Workflow

Describe your experience using git for this lab (don't use markdown list for this answer)

TODO: Reflect on your git workflow for this lab. How many commits did you make? What was your commit strategy? Did you make descriptive commit messages? How did git help you track your progress and changes? If you worked with a partner, how did you coordinate your git workflow?

## Challenges

Describe the main challenges you faced during this lab (don't use markdown list for this answer)

TODO: Reflect on the challenges you encountered while completing this lab. Consider challenges with: dictionary design and nested dictionaries, working with hardware sensors (DHT22, LDR, buzzer), reading sensor data and handling errors, integrating the three modules together, debugging your code, and any other difficulties you faced. Be specific about what made these challenges difficult and how you worked to overcome them.

## Learning

What are the most important things you learned about dictionaries, hardware integration, and sensor data during this lab? (don't use markdown list for this answer)

TODO: Reflect on what you learned from this lab. Consider: how dictionaries help organize sensor data, the advantages of using dictionaries over lists for this type of program, what you learned about dictionary methods like .items(), .values(), .keys(), how nested dictionaries work, what you learned about working with hardware sensors (DHT22 temperature/humidity, LDR photoresistor, passive buzzer), how sensor readings are converted to usable data, the importance of error handling when reading sensors, and how multiple modules can work together in an integrated system.

## Improvements

If you were to complete this assignment again, what would you do differently? (use a markdown list for this answer)

- **Dictionary design:** TODO: What would you change about how you structured your dictionaries? Would you use different keys, organize the data differently, or add more information to each entry?

- **Code organization:** TODO: How would you improve your code structure, function design, or error handling? What would make your code more readable or maintainable?

- **Hardware integration:** TODO: What would you do differently when working with the sensors and buzzer? How could you improve sensor reading reliability or error handling?

- **Testing approach:** TODO: How would you test your code more thoroughly? What testing strategies would help catch bugs earlier?

- **Time management:** TODO: How would you better plan your time for completing this lab? What would you start earlier or spend more time on?
