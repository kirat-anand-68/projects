public class methodChallenge {
    public static void main(String[] args) {
                int highScorePosition  = calculateHighScorePosition(500);
                displayHighScorePosition("kirat",highScorePosition);
                highScorePosition  = calculateHighScorePosition(1100);    /* no need to put again int infront of the highscore as it already being declared*/
                displayHighScorePosition("Avleen",highScorePosition);
                highScorePosition  = calculateHighScorePosition(700);
                displayHighScorePosition("Harleen",highScorePosition);
                highScorePosition  = calculateHighScorePosition(90);
                displayHighScorePosition("Ashpreet",highScorePosition);


            }

            public static void displayHighScorePosition(String PlayerName,int highScorePosition) {
                System.out.println(PlayerName + " Managed to get the Position " + highScorePosition +"on the Score list");

            }

            public static int calculateHighScorePosition(int playerScore) {
                if(playerScore>=1000){
                    return 1;
                }
                else if(playerScore >=500 && playerScore <1000){
                    return 2;
                }
                else if(playerScore >=100 && playerScore<500){
                    return 3;
                }
                else {
                    return 4;
                }

            }
        }



