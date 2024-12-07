package day06;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

class Guard {
    int i;
    int j;
    String dir;
    ArrayList<char[]> map;
    boolean done = false;
    ArrayList<State> states = new ArrayList<>();
    int obstructions = 0;

    public Guard(int i, int j, String dir, ArrayList<char[]> map) {
        this.i = i;
        this.j = j;
        this.dir = dir;
        this.map = map;
    }



    public void walk() {
        if (isTrappable()) {
            obstructions++;
            System.out.println("Found possible trap by turning " + getTurnedDirection(dir) + " at " + i + " " + j);
        }

        switch (dir) {
            case "up" -> walkUp();
            case "down" -> walkDown();
            case "left" -> walkLeft();
            case "right" -> walkRight();
            default -> System.out.println("Error");
        }
    }

    public void walkUp() {
        char test = map.get(i)[j];
        if (map.get(i)[j] == '-') {
            map.get(i)[j] = '+';
        }
        else {
            map.get(i)[j] = '|';
        }
        System.out.println("Walk up" + " i" + i + " j" + j + "    was " + test + "    wrote " + map.get(i)[j]);
        if (i - 1 < 0) {
            done = true;
        }
        else if (map.get(i-1)[j] == '.' || map.get(i-1)[j] == '+' || map.get(i-1)[j] == '|' || map.get(i-1)[j] == '-') {
            i = i - 1;
        }
        else {
            dir = "right";
        }
    }
    public void walkDown() {
        char test = map.get(i)[j];
        if (map.get(i)[j] == '-') {
            map.get(i)[j] = '+';
        }
        else {
            map.get(i)[j] = '|';
        }
        System.out.println("Walk down" + " i" + i + " j" + j + "    was " + test +  "    wrote " + map.get(i)[j]);
        if (i + 1 >= map.size()) {
            done = true;
        }
        else if (map.get(i-1)[j] == '.' || map.get(i+1)[j] == '+' || map.get(i+1)[j] == '|' || map.get(i+1)[j] == '-') {
            i = i + 1;
        }
        else {
            dir = "left";
        }
    }
    public void walkLeft() {
        char test = map.get(i)[j];
        if (map.get(i)[j] == '|') {
            map.get(i)[j] = '+';
        }
        else {
            map.get(i)[j] = '-';
        }
        System.out.println("Walk Left" + "i" + i + "j" + j + "    was " + test + "    wrote " + map.get(i)[j]);
        if (j - 1 < 0) {
            done = true;
        }
        else if (map.get(i)[j-1] == '.' || map.get(i)[j-1] == '+' || map.get(i)[j-1] == '|' || map.get(i)[j-1] == '-') {
            j = j - 1;
        }
        else {
            dir = "up";
        }
    }
    public void walkRight() {
        char test = map.get(i)[j];
        if (map.get(i)[j] == '|') {
            map.get(i)[j] = '+';
        }
        else {
            map.get(i)[j] = '-';
        }
        System.out.println("Walk right" + " i" + i + " j" + j + "    was " + test + "  wrote " + map.get(i)[j]);
        if (j + 1 >= map.get(i).length) {
            done = true;
        }
        else if (map.get(i)[j+1] == '.' || map.get(i)[j+1] == '+' || map.get(i)[j+1] == '|' || map.get(i)[j+1] == '-') {
            j = j + 1;
        }
        else {
            dir = "down";
        }
    }

    private String getTurnedDirection(String dir) {
        String turnedDirection = "";
        switch (dir) {
            case "up" -> turnedDirection = "right";
            case "down" -> turnedDirection = "left";
            case "left" -> turnedDirection = "up";
            case "right" -> turnedDirection = "down";
        }
        return turnedDirection;
    }

    public int[] solve() {
        while (!done) {
            walk();
        }
        return new int[]{countX(), obstructions};
    }

    private int countX() {
        int count = 0;
        for (char[] arr : map) {
            for (char c : arr) {
                if (c == 'X' || c == '+' || c == '-' || c == '|') {
                    count ++;
                }
            }
        }
        return count;
    }

    private boolean isTrappable() {
        switch (dir) {
            case "left": {
                for (int i = this.i; i >= 0; i--) {
                    switch (map.get(i)[j]) {
                        case ('|') -> {
                            return true;
                        }
                        case ('+') -> {
                            return true;
                        }
                        case ('#') -> {
                            break;
                        }
                    }
                }
            }
            case "right": {
                for (int i = this.i; i < map.size(); i++) {
                    switch (map.get(i)[j]) {
                        case ('|') -> {
                            return true;
                        }
                        case ('+') -> {
                            return true;
                        }
                        case ('#') -> {
                            break;
                        }
                    }
                }
            }
            case "up": {
                for (int j = this.j; j < map.get(i).length; j++) {
                    switch (map.get(i)[j]) {
                        case ('-') -> {
                            return true;
                        }
                        case ('+') -> {
                            return true;
                        }
                        case ('#') -> {
                            break;
                        }
                    }
                }
            }
            case "down": {
                for (int j = this.j; j >= 0; j--) {
                    switch (map.get(i)[j]) {
                        case ('-') -> {
                            return true;
                        }
                        case ('+') -> {
                            return true;
                        }
                        case ('#') -> {
                            break;
                        }
                    }
                }
            }
        }
        return false;
    }
}