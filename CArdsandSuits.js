function getCard(){
    const values=[
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'j',
        'Q',
        'K',
        'A'];

const ValIdx=Math.floor(Math.random()*values.length);
const value=values[ValIdx]

const suits=['clubs',
'spades',
'hearts',
'diamonds'];
const SuitIdx=Math.floor(Math.random()*suits.length);
const suit=suits[SuitIdx]
return{value:value,suit:suit};
}
console.log(getCard())
