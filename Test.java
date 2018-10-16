/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jeopar;

import java.io.IOException;

/**
 *
 * @author Acer
 */
public class Test 
{
    public static void main(String args[]) throws IOException
    {
        String command = "python /c start python C:\\Users\\Rohit\\.spyder-py3\\read.py";
        //Process p = Runtime.getRuntime().exec(command + param );
        Process p = Runtime.getRuntime().exec(command);
    }
}
