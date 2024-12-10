package day06;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

class Guard {
    int i;
    int j;
    String dir;
    ArrayList<String[]> map;
    boolean done = false;
    ArrayList<State> states = new ArrayList<>();
    int obstructions = 0;
    private boolean isPaused = false;

    public Guard(int i, int j, String dir, ArrayList<String[]> map) {
        this.i = i;
        this.j = j;
        this.dir = dir;
        this.map = map;
    }



    public void walk() throws InfinityException{
        if (!isPaused) {
            System.out.println("This happens");
            isPaused = true;
            ArrayList<String[]> pausedMap = new ArrayList<>(map);
            String pausedDir = dir;
            switch (dir) {
                case "up" -> map.get(i - 1)[j] = "#";
                case "down" -> map.get(i + 1)[j] = "#";
                case "left" -> map.get(i)[j - 1] = "#";
                case "right" -> map.get(i)[j + 1] = "#";
            }
            try {
                solve();
            }
            catch (InfinityException e) {
                obstructions += 1;
            }
            finally {
            dir = pausedDir;
            isPaused = false;
            map = pausedMap;
            done = false;
            }
        }
        else {
            System.out.println("Regular walk!");
        }
        switch (dir) {
            case "up" -> walkUp();
            case "down" -> walkDown();
            case "left" -> walkLeft();
            case "right" -> walkRight();
            default -> System.out.println("No direction found");
        }
    }

    public void walkUp() throws InfinityException {
        if (map.get(i)[j].contains("u")) {
            throw new InfinityException("This was thrown to increment the number of loops");
        }
        map.get(i)[j] = map.get(i)[j] + "u";

        if (i - 1 < 0) {
            done = true;
        }
        else if (map.get(i - 1)[j].contains("#")) {
            dir = "right";
        }
        else {
            i --;
        }
    }
    public void walkDown() throws InfinityException {
        if (map.get(i)[j].contains("d")) {
            throw new InfinityException("This was thrown to increment the number of loops");
        }
        map.get(i)[j] = map.get(i)[j] + "d";

        if (i + 1 >= map.size()) {
            done = true;
        }
        else if (map.get(i+1)[j].contains("#")) {
            dir = "left";
        }
        else {
            i ++;
        }
    }
    public void walkLeft() throws InfinityException {
        if (map.get(i)[j].contains("l")) {
            throw new InfinityException("This was thrown to increment the number of loops");
        }
        map.get(i)[j] = map.get(i)[j] + 'l';

        if (j - 1 < 0) {
            done = true;
        }
        else if (map.get(i)[j-1].contains("#")) {
            dir = "up";
        }
        else {
            j--;
        }
    }
    public void walkRight() throws InfinityException {
        if (map.get(i)[j].contains("r")) {
            throw new InfinityException("This was thrown to increment the number of loops");
        }
        map.get(i)[j] = map.get(i)[j] + 'r';

        if (j + 1 >= map.get(i).length) {
            done = true;
        }
        else if (map.get(i)[j+1].contains("#")) {
            dir = "down";
        }
        else {
            j ++;
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

    public int[] solve() throws InfinityException {
        map.get(i)[j] = ".";
        while (!done) {
            walk();
        }
        for (String[] arr : map) {
            System.out.println(Arrays.toString(arr));
        }
        return new int[]{countVisited(), obstructions};
    }

    private int countVisited() {
        int count = 0;
        for (String[] arr : map) {
            for (String s : arr) {
                if (s.contains("u") || s.contains("l") || s.contains("r") || s.contains("d") ) {
                    count ++;
                }
            }
        }
        return count;
    }
}