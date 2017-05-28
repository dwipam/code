package com;

import java.lang.reflect.Array;

/**
 * Created by dwipam on 5/27/17.
 */
public class BallGame{
    public static class _ {
        public int checker(int[][] maze, int[] start, int[] dest) {
            int[][] dist = new int[maze.length][maze[0].length];
            for (int i = 0; i < maze.length; i++) {
                for (int j = 0; j < maze[0].length; j++) {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }
            dist[start[0]][start[1]] = 0;
            dfs(maze, dist, start, dest);
            for (int[] i:dist) {
                for(int j=0;j<maze[0].length;j++)
                    System.out.print(i[j]+"\t");
                System.out.println("\n");
                }


            return dist[dest[0]][dest[1]] == Integer.MAX_VALUE ? -1 : dist[dest[0]][dest[1]];
        }

        public void dfs(int[][] maze, int[][] dist, int[] start, int[] dest) {
            int[][] next = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
            for (int[] i : next) {
                int x = start[0] + i[0];
                int y = start[1] + i[1];
                int count = 0;
                while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0 ) {
                    x += i[0];
                    y += i[1];
                    count += 1;
                }
                if (dist[start[0]][start[1]] + count < dist[x - i[0]][y - i[1]]) {
                    dist[x - i[0]][y - i[1]] = dist[start[0]][start[1]] + count;
                    dfs(maze, dist, new int[]{x - i[0], y - i[1]}, dest);
                }

            }
        }
    }
        public static void main(String args[]) throws Exception {
            _ obj = new _();
            int[][] maze = {{0,0,1,0,0},{0,0,0,0,0},{0,0,0,1,0},{1,1,0,1,1},{0,0,0,0,0}};
            int[] start = {0,1};
            int[] dest = {4,4};
            System.out.print(obj.checker(maze,start,dest));
        }
    }
