package programmers;

// 43165

class targetNum {
    int[] globalNumbers;
    int globalTarget;
    public int solution(int[] numbers, int target) {
        globalNumbers = numbers;
        globalTarget = target;
        return DFS(0,0);
    }

    private int DFS(int current, int depth) {
        if (depth == globalNumbers.length) {
            if (current == globalTarget) return 1;
            else return 0;
        }
        else {
            return DFS(current+globalNumbers[depth], depth+1)
            + DFS(current-globalNumbers[depth], depth+1);
        }
    }
}