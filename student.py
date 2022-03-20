import pyautoguiimport os
import platform

global listStd ~Making ListStd As Super Global Variable
listStd = ["yugesh", "kishor", "gajen", "Gopi"] ~List Of Students

def manageStudent(): ~Function For The Student Management System

	x = "~" * 30
		y = "=" * 28
			global bye ~Making Bye As Super Global Variable
				bye = "\n {}\n~ {} ~\n~ ===> Brought To You By <===  ~\n~ ===> code-projects.org <===  ~\n~ {} ~\n {}".format(x, y, y, x) ~ Will Print GoodBye Message

					~Printing Welcome Message And options For This Program
						print(""" 
						
						  ------------------------------------------------------
						   |======================================================| 
						    |======== Welcome To Student Management System	========|
							 |======================================================|
							   ------------------------------------------------------
							   
							   Enter 1 : To View Student's List 
							   Enter 2 : To Add New Student 
							   Enter 3 : To Search Student 
							   Enter 4 : To Remove Student 
							   		
									   		""")
											   
											   	try: ~Using Exceptions For Validation
												   		userInput = int(input("Please Select An Above Option: ")) ~Will Take Input From User
														   	except ValueError:
																   		exit("\nHy! That's Not A Number") ~Error Message
																		   	else:
																				   		print("\n") ~Print New Line
																						   
																						   	~Checking Using Option	
																							   	if(userInput == 1): ~This Option Will Print List Of Students
																								   		print("List Students\n")  
																										   		for students in listStd:
																													   			print("=> {}".format(students))
																																   
																																   	elif(userInput == 2): ~This Option Will Add New Student In The List
																																	   		newStd = input("Enter New Student: ")
																																			   		if(newStd in listStd): ~This Condition Checking The New Student Is Already In List Ur Not
																																					   			print("\nThis Student {} Already In The Database".format(newStd))  ~Error Message
																																								   		else:	
																																											   			listStd.append(newStd)
																																														   			print("\n=> New Student {} Successfully Add \n".format(newStd))
																																																	   			for students in listStd:
																																																					   				print("=> {}".format(students))	
																																																									   )