# Week 5 Review

## 1 [shadow-maker.py]
Your goal is to write a function called `makeShadow` that accepts one parameter, a Shape object, and then will create and return a shape that "shadows" the shape argument. Consider the two shapes shown in the window below: 

![test_shapes](/images/test_shapes.png)

If we were call the `makeShadow` function passing the Circle object as an argument, then the `makeShadow` function would return another Circle object that would be a shadow for the Circle argument. If we drew that shadow Circle object in the window, without the original Circle object it would look like this (ignore the mouse pointer):

![circle_shadow](/images/circle_shadow.png)

Then if we drew both shapes in the window, the shadow Circle first, then the original Circle object, it would look like this:

![shadowed_circle](/images/shadowed_circle.png)

That shadow Circle is offset 4 pixels to the right and 4 pixels down from the location of the original Circle object. Its outline and fill are a lighter gray. 

Your `makeShadow` method should also be able to create and return a shadow for any type of Shape object including the Rectangle object. If used the `makeShadow` function to create a shadow Rectangle object, and drew in both the Rectangle Object and its shadow object, and then we have the image:

![test_shapes_with_shadows](/images/test_shapes_with_shadows.png)

Included in your `shadow-maker.py` file is a function named `testShadowMaker` that draws the Circle and Rectangle objects as shown above. You are encouraged to modify the `testShadowMaker` method to verify that your `makeShadow` function is working as you expect.


## 2 [doc-stats.py]
What words counted as "actual" words has varied over time. The articles `a`, `an`, and `the` did not always count as words when counting words in a document. Your goal is to extend the doc-stats program to additionally report the number of words in the document not including the articles. You have also been provided three text files for testing: `haiku.txt`, `gettysburg.txt`, and `mobydick.txt`.

An example result:

```
Enter your text file name: mobydick.txt

******* mobydick.txt ******* 
Total Lines: 15604
Total Chars: 512293
Total Words: 115314
Total Non-Article Words: 105479
```

HINT: Are `an`, `aN`, and `AN` the same things?

## 3 [my-refactored-house.py]
Recall the majesty that was your house drawing with its interactive feature. If you were to investigate how you wrote that program, you may discover there is a lot of redundancy which you now have the ability to reduce effectively. You have two goals:

1. refactor your house drawing in this new drawing program to reduce the repetition of code segments using functions and parameters, as well as separating concerns (e.g., drawing the roof is a separate concern from drawing windows)
1. add a new, repeated element to your drawing. This repeated element should be drawn at least three times in your drawing and include more than one type of graphical object as well as some color(s). As an example, which you now cannot use, below is a window (1 rectangle filled, 2 lines) that I could repeat three times in my drawing. Other examples might include trees, clouds, or airplanes.

![window](/images/window.png)

## 4 [area-computer-menu.py]
You are working with a team to develop a program for computing the area of different shapes. Your role on the team is to develop the menu system and _only the menu system_: not any other feature such as the actual shape area computations. The menu system is specified to do the following:

* Output a welcome message
* Output a menu listing the input options: `tri` to compute the area of a triangle, `trap` to compute the area of a trapezoid, `quit` to quit the program and one other input of your choice
* Accept input from the user for their choice, but validate that the input is one of the acceptable options. If the input is not acceptable, then the user should need to input another value until the option is acceptable

Your solution should include at least three functions:

* a function for printing out the welcome information and list of menu options
* a function for getting the user's input that returns their valid choice, 
* a `main` function which calls these functions in the appropriate order, and outputs what the valid choice is (NOTE: the valid choice is to be output in the `main` function, not the function which is getting the input).

An example interaction with a correct program:

```
Welcome to the area computation tool!

****** MENU ******
tri    Compute area of a triangle
trap   Compute area of a trapezoid
????   THIS_WOULD_BE_YOUR_CHOICE_DON'T_OUTPUT_THIS
quit   Quit the tool

Please enter your choice: butter
'butter' is an invalid choice
Please enter your choice: tri
You chose: tri
```
