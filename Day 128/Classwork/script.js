    let userScore = 0;
    let computerScore = 0;

    function playGame(userChoice) {
      const choices = ['rock', 'paper', 'scissors'];
      const computerChoice = choices[Math.floor(Math.random() * 3)];


      let resultText = '';
      if (userChoice === computerChoice) {
        resultText = 'ფრე!';
      } else if (
        (userChoice === 'rock' && computerChoice === 'scissors') ||
        (userChoice === 'paper' && computerChoice === 'rock') ||
        (userChoice === 'scissors' && computerChoice === 'paper')
      ) {
        userScore++;
        resultText = 'შენ მოიგე!';
      } else {
        computerScore++;
        resultText = 'კომპიუტერმა მოიგო!';
      }

      document.getElementById('user-score').textContent = userScore;
      document.getElementById('computer-score').textContent = computerScore;
      document.getElementById('result').textContent = resultText;
      document.getElementById('status').textContent = `შენ აირჩიე: ${userChoice}, კომპიუტერმა: ${computerChoice}`;
    }
