package day06;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("inputs/test.txt");
        Scanner reader = new Scanner(file);
        ArrayList<String[]> contents = new ArrayList<>();
        while (reader.hasNextLine()) {
            contents.add(reader.nextLine().split(""));
        }

        // Identify the guard


        int guardPosI = -1;
        int guardPosJ = -1;
        String guardDirection = "";


        int checked = 0;
        for (int i = 0; i < contents.size(); i++) {
            for (int j = 0; j < contents.get(i).length; j++) {
                if (!contents.get(i)[j].contains("#") && !contents.get(i)[j].contains(".")) {
                    guardPosI = i;
                    guardPosJ = j;
                    switch (contents.get(i)[j]) {
                        case "^" -> guardDirection = "up";
                        case "v" -> guardDirection = "down";
                        case "<" -> guardDirection = "left";
                        case ">" -> guardDirection = "right";

                    }
                }
            }
        }
        Guard guard = new Guard(guardPosI, guardPosJ, guardDirection, contents);
        try {
            int[] result = guard.solve();
            System.out.println(result[0] + "   " + result[1]);
        }
        catch (InfinityException e) {
            System.out.println(e.getMessage());
            System.out.println("^^^^^^THIS WAS THROWN IN MAIN^^^^^");
        }
    }
}
