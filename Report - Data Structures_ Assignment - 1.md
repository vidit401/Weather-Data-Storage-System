Data Structures: Assignment \- 1  
Weather Data Storage System

**Name:** Vidit Bansal  
**Roll no. \-** 2401420018  
**Course:** B.Tech CSE (Data Science)

**Problem Statement**   
The goal is to create a Weather Data Storage System that organises temperature data for different cities and years. The system should allow users to add, remove, and get records. It should also display data by years, by cities, show only available data, and analyse the complexity of the operations. The system uses a simple menu-driven program for interaction.

**Assignment Objectives**

* Understand the use of arrays and mapping in Python.   
* Learn to build a simple Abstract Data Type (ADT) for storing weather data.   
* Gain practice with user input and menu-driven programs.   
* Cleanly handle missing data.   
* Analyse the time and space complexity of operations. 

**Record Class**   
The Record class represents a single entry with three attributes: 

* Date (string)  
* City (string)  
* Temperature (float value) 

**WeatherSystemClass**   
The WeatherSystem class is the main storage system using a 2D array (years × cities). 

**It provides the following methods:** 

* add\_record (year, city, temperature): Add a new record.   
* remove\_record (year, city): Remove a record (set to None).   
* get\_record (city, year): Get the temperature of a city in a year.   
* show\_by\_years(): Show all data organised by years.   
* show\_by\_cities(): Show all data organised by cities.   
* show\_available(): Show only available data (ignores None).   
* show\_complexity(): Show time and space complexity of operations.

**Menu-driven Program** 

**The main() function creates a menu with the following options for the user:** 

1\) Add data   
2\) Remove data   
3\) Get data   
4\) Show data by years   
5\) Show data by cities   
6\) Show available data   
7\) Show complexity info   
8\) Exit program

**Sparse Data Handling**   
Sparse data is handled by storing None values for missing records. This way, only available entries are displayed when calling show\_available().

**Complexity Analysis** 

* add\_record: O(1) time, O(1) space   
* remove\_record: O(1) time, O(1) space   
* get\_record: O(1) time, O(1) space   
* show\_by\_years: O(n\*m) time, O(1) space   
* show\_by\_cities: O(n\*m) time, O(1) space   
* storage: O(n\*m) space where n \= number of years, m \= number of cities

**Conclusion**

This project implements a simple weather data system using arrays and mappings. It gives practice with ADTs, menu-driven programming, and handling sparse data. The complexity analysis shows that basic operations are efficient, while traversals depend on the size of the dataset. This assignment helps build a strong foundation in programming with arrays and simple data structures.

