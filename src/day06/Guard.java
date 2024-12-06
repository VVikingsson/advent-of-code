package day06;

import java.util.ArrayList;

class Guard {
    int i;
    int j;
    String dir;
    ArrayList<char[]> map;
    boolean done = false;

    public Guard(int i, int j, String dir, ArrayList<char[]> map) {
        this.i = i;
        this.j = j;
        this.dir = dir;
        this.map = map;
    }

    public void walk() {
        map.get(i)[j] = 'X';

        switch (dir) {
            case "up" -> walkUp();
            case "down" -> walkDown();
            case "left" -> walkLeft();
            case "right" -> walkRight();
            default -> System.out.println("Error");
        }
    }

    public void walkUp() {
        System.out.println("up" + " i" + i + " j" + j);
        if (i - 1 < 0) {
            done = true;
        }
        else if (map.get(i-1)[j] == '.' || map.get(i-1)[j] == 'X') {
            i = i - 1;
        }
        else {
            dir = "right";
        }
    }
    public void walkDown() {
        System.out.println("down" + " i" + i + " j" + j);
        if (i + 1 >= map.size()) {
            done = true;
        }
        else if (map.get(i+1)[j] == '.' || map.get(i+1)[j] == 'X') {
            i = i + 1;
        }
        else {
            dir = "left";
        }
    }
    public void walkLeft() {
        System.out.println("Left" + "i" + i + "j" + j);
        if (j - 1 < 0) {
            done = true;
        }
        else if (map.get(i)[j-1] == '.' || map.get(i)[j-1] == 'X') {
            j = j - 1;
        }
        else {
            dir = "up";
        }
    }
    public void walkRight() {
        System.out.println("right" + " i" + i + " j" + j);
        if (j + 1 >= map.get(i).length) {
            done = true;
        }
        else if (map.get(i)[j+1] == '.' || map.get(i)[j+1] == 'X') {
            j = j + 1;
        }
        else {
            dir = "down";
        }
    }

    public int solve() {
        while (!done) {
            walk();
        }
        return countX();
    }

    private int countX() {
        int count = 0;
        for (char[] arr : map) {
            for (char c : arr) {
                if (c == 'X') {
                    count ++;
                }
            }
        }
        return count;
    }

}