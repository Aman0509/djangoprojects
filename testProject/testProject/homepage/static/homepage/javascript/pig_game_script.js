'use strict';

const playerEl0 = document.querySelector('.player--0');
const playerEl1 = document.querySelector('.player--1');
const scoreEl0 = document.getElementById('score--0');
const scoreEl1 = document.getElementById('score--1');
const currentEl0 = document.getElementById('current--0');
const currentEl1 = document.getElementById('current--1');
const diceEl = document.querySelector('.dice');
const btnNewEl = document.querySelector('.btn--new');
const btnRollEl = document.querySelector('.btn--roll');
const btnHoldEl = document.querySelector('.btn--hold');

let playing, totScore, currentScore, activePlayer;

const init = function () {
  playing = true;
  totScore = [0, 0];
  currentScore = 0;
  activePlayer = 0;

  currentEl0.textContent = 0;
  currentEl1.textContent = 0;
  scoreEl0.textContent = 0;
  scoreEl1.textContent = 0;

  diceEl.classList.add('hidden');
  playerEl0.classList.remove('player--winner');
  playerEl1.classList.remove('player--winner');
  playerEl1.classList.remove('player--active');
  playerEl0.classList.add('player--active');
};
init();

const switchPlayer = function () {
  document.getElementById(`current--${activePlayer}`).textContent = 0;
  currentScore = 0;
  playerEl0.classList.toggle('player--active');
  playerEl1.classList.toggle('player--active');
  activePlayer = activePlayer === 0 ? 1 : 0;
};

btnRollEl.addEventListener('click', function () {
  // Generating the Random number
  if (playing) {
    let diceNum = Math.trunc(Math.random() * 6) + 1;

    // Displaying the dice photo corresponding to diceNum
    diceEl.classList.remove('hidden');
    diceEl.src = `/static/homepage/image/dice-${diceNum}.png`;

    if (diceNum !== 1) {
      currentScore += diceNum;
      document.getElementById(
        `current--${activePlayer}`
      ).textContent = currentScore;
      if (totScore[activePlayer] + currentScore >= 100) {
        playing = false;
        document.getElementById(`score--${activePlayer}`).textContent =
          totScore[activePlayer] + currentScore;
        diceEl.classList.add('hidden');
        document
          .querySelector(`.player--${activePlayer}`)
          .classList.add('player--winner');
        document
          .querySelector(`.player--${activePlayer}`)
          .classList.remove('player--active');
      }
    } else {
      switchPlayer();
    }
  }
});

btnHoldEl.addEventListener('click', function () {
  if (playing) {
    // Add Current Score to active player's Score in the webpage
    totScore[activePlayer] += currentScore;
    document.getElementById(`score--${activePlayer}`).textContent =
      totScore[activePlayer];
    switchPlayer();
  }
});

btnNewEl.addEventListener('click', init);

//During learning time I defined 'new button' functionality like below, but we can define a init function first and then call it.
//  As shown above
/*btnNewEl.addEventListener('click', function () {
  diceEl.classList.add('hidden');
  document
    .querySelector(`.player--${activePlayer}`)
    .classList.remove('player--winner');
  document.querySelector(`.player--0`).classList.add('player--active');
  currentEl0.textContent = 0;
  currentEl1.textContent = 0;
  scoreEl0.textContent = 0;
  scoreEl1.textContent = 0;
  totScore[0] = totScore[1] = 0;
  playing = true;
  currentScore = 0;
  activePlayer = 0;
});*/
