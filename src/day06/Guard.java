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

    public Guard(int i, int j, String dir, ArrayList<String[]> map) {
        this.i = i;
        this.j = j;
        this.dir = dir;
        this.map = map;
    }



    public void walk() {
        //System.out.println("Current direction: " + dir + " Current location: " + i + " " + j);
        if (isTrappable(dir, i, j)) {
            obstructions++;
            System.out.println("Found possible trap going " + dir + " turning " + getTurnedDirection(dir) + " at " + (1 +i) + " " + (1+j));
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
    public void walkDown() {
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
    public void walkLeft() {
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
    public void walkRight() {
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

    public int[] solve() {
        map.get(i)[j] = ".";
        while (!done) {
            walk();
        }
        return new int[]{countVisited(), obstructions};
    }

    private int countVisited() {
        int count = 0;
        for (String[] arr : map) {
            System.out.println(Arrays.toString(arr));
            for (String s : arr) {
                if (s.contains("u") || s.contains("l") || s.contains("r") || s.contains("d") ) {
                    count ++;
                }
            }
        }
        return count;
    }

    private boolean isTrappable(String dir, int x, int y) {
        switch (dir) {
            case "left": {
                for (int i = x; i > 0; i--) {
                    if (map.get(i)[y].contains("u")) {
                        return true;
                    }
                    if (map.get(i-1)[y].contains("#")) {
                        if (isTrappable("up", i, y)) { return true; }
                        else { break; }
                    }
                }
                break;
            }
            case "right": {
                for (int i = x; i < map.size() - 1; i++) {
                    if (map.get(i)[y].contains("d")) {
                        return true;
                    }
                    if (map.get(i+1)[y].contains("#")) {
                        if (isTrappable("down", i, y)) {
                            return true;
                        }
                        else { break; }
                    }
                }
                break;
            }
            case "up": {
                for (int j = y; j < map.get(i).length - 1; j++) {
                    if (map.get(x)[j].contains("r")) {
                        return true;
                    }
                    if (map.get(x)[j].contains("#")) {
                        if (isTrappable("down", x, j)) {
                            return true;
                        }
                        else { break; }
                    }
                }
                break;
            }
            case "down": {
                for (int j = y; j > 0; j--) {
                    if (map.get(x)[j].contains("l")) {
                        return true;
                    }
                    if (map.get(x)[j-1].contains("#")) {
                        if (isTrappable("up", x, j)) {
                            return true;
                        }
                        else { break; }
                    }
                }
                break;
            }
        }
        return false;
    }
}