      * *****************************************************************
      * Program name:    SIMPLE-CALCULATOR                               
      * Original author: GUNKNARD.                               
      *
      * Maintenence Log                                              
      * Date      Author        Maintenance Requirement               
      * --------- ------------  --------------------------------------- 
      * 01/01/08 MYNAME  Created for COBOL class         
      *                                                               
      *****************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID.  SIMPLE-CALCULATOR.
       AUTHOR. GUNKNARD.
       INSTALLATION. COBOL DEVELOPMENT CENTER. 
       DATE-WRITTEN. 01/01/08. 
       DATE-COMPILED. 01/01/08. 
       SECURITY. NON-CONFIDENTIAL.
      *****************************************************************
      *****************************************************************
       DATA DIVISION.
            
       WORKING-STORAGE SECTION.
       01  NUM1 PIC 9(5).
       01  NUM2 PIC 9(5).
       01  RESULT PIC 9(5).
       01  OPERATOR PIC X.
      *****************************************************************
      *****************************************************************
      ******************************************************************
       PROCEDURE DIVISION.
           DISPLAY "Enter first number: ".
           ACCEPT NUM1.

           DISPLAY "Enter operator (+, -, *, /): ".
           ACCEPT OPERATOR.

           DISPLAY "Enter second number: ".
           ACCEPT NUM2.

           PERFORM CALCULATE-RESULT.

           DISPLAY "Result: " RESULT.

           STOP RUN.

      *****************************************************************
      *****************************************************************
       CALCULATE-RESULT.
           IF OPERATOR = "+" THEN
               ADD NUM1 TO NUM2 GIVING RESULT
           ELSE IF OPERATOR = "-" THEN
               SUBTRACT NUM2 FROM NUM1 GIVING RESULT
           ELSE IF OPERATOR = "*" THEN
               MULTIPLY NUM1 BY NUM2 GIVING RESULT
           ELSE IF OPERATOR = "/" THEN
               DIVIDE NUM1 BY NUM2 GIVING RESULT
           END-IF.

      *****************************************************************
      *****************************************************************
       