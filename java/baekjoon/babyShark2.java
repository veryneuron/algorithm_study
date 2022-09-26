package baekjoon;
// import java.util.*;
// import java.io.*;

// public class Main {
//     static int N, M;
//     static int[][] MAP;
//     public static void main (String[] args) throws IOException{
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         N = Integer.parseInt(st.nextToken());
//         M = Integer.parseInt(st.nextToken());
//         MAP = new int[N][M];
//         for (int i=0; i < N; i++) {
//             StringTokenizer oneLine = new StringTokenizer(br.readLine());
//             for (int j=0; j < M; j++) {
//                 MAP[i][j] = Integer.parseInt(oneLine.nextToken());
//             }
//         }

//         int safeDist = 0;
        
//         for (int i=0; i < N; i++) {
//             for (int j=0; j < M; j++) {
//                 if (MAP[i][j] != 1) {
//                     int temp = bfs(i, j);
//                     if (temp > safeDist) safeDist = temp;
//                 }
//             }
//         }
//         System.out.println(safeDist);
//     }

//     private static int bfs(int row, int col) {
//         boolean[][] visited = new boolean[N][M];
//         visited[row][col] = true;
//         Deque<Position> dq = new ArrayDeque<>();
//         dq.addLast(new Position(row, col, 0));
//         int minDist = Integer.MAX_VALUE;
//         while (!dq.isEmpty()) {
//             Position now = dq.pollFirst();
//             if (MAP[now.row][now.col] == 1) {
//                 if (minDist > now.dist) {
//                     minDist = now.dist;
//                 }
//             }
//             int[][] dpList = {{1,0},{0,1},{1,1},{-1,0},{0,-1},{-1,-1},{1,-1},{-1,1}};
//             for (var dp : dpList) {
//                 int newRow = now.row + dp[0];
//                 int newCol = now.col + dp[1];
//                 if (0 <= newRow && newRow < N && 0 <= newCol && newCol < M) {
//                     if (visited[newRow][newCol] == false) {
//                         visited[newRow][newCol] = true;
//                         dq.addLast(new Position(newRow, newCol, now.dist+1));
//                     }
//                 }
//             }
//         }
//         return minDist;
//     }

//     static class Position {
//         int row;
//         int col;
//         int dist;
//         public Position (int r, int c, int d) {
//             this.row = r;
//             this.col = c;
//             this.dist = d;
//         }
//     }
// }

// 다른 사람의 풀이
// for (int i = 0; i < N; i++) {
//     st = new StringTokenizer(br.readLine());
//     for (int j = 0; j < M; j++) {
//         map[i][j] = st.nextToken().equals("1") ? true : false;
//         if(map[i][j]) q.add(new El(i, j, 0));
//     }
// }
// 처럼 처음부터 상어 좌표를 전부 큐에 넣으면 효율적임!
// 상어 기준으로 bfs로 범위 넓혀가면서 최대값 구하는것
// gps로 거리 구하는것과 유사
// 상하좌우 하는 다른방법

// int[] dir = {-1, 0, 1};
// for (int i = 0; i < 3; i++) {
//     for (int j = 0; j < 3; j++) {
        
//         if(i==1 && j==1) continue;
        
//         int xx = el.x + dir[i];
//         int yy = el.y + dir[j];

// 큐 수정본

import java.util.*;
import java.io.*;

public class babyShark2 {
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] MAP = new int[N][M];
        boolean[][] visited = new boolean[N][M];
        Deque<Position> dq = new ArrayDeque<>();
        for (int i=0; i < N; i++) {
            StringTokenizer oneLine = new StringTokenizer(br.readLine());
            for (int j=0; j < M; j++) {
                MAP[i][j] = Integer.parseInt(oneLine.nextToken());
                if (MAP[i][j] == 1) {
                    visited[i][j] = true;
                    dq.addLast(new Position(i, j, 0));
                }
            }
        }
        int safeDist = 0;
        while (!dq.isEmpty()) {
            Position now = dq.pollFirst();
            if (now.dist > safeDist) safeDist = now.dist;
            int[][] dpList = {{1,0},{0,1},{1,1},{-1,0},{0,-1},{-1,-1},{1,-1},{-1,1}};
            for (var dp : dpList) {
                int newRow = now.row + dp[0];
                int newCol = now.col + dp[1];
                if (0 <= newRow && newRow < N && 0 <= newCol && newCol < M) {
                    if (visited[newRow][newCol] == false) {
                        visited[newRow][newCol] = true;
                        dq.addLast(new Position(newRow, newCol, now.dist+1));
                    }
                }
            }
        }
        System.out.println(safeDist);
    }

    static class Position {
        int row;
        int col;
        int dist;
        public Position (int r, int c, int d) {
            this.row = r;
            this.col = c;
            this.dist = d;
        }
    }
}