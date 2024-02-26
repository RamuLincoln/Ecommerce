
let launchDate = new Date("Oct 30, 2022 12:00:00").getTime();
console.log(launchDate)

let timer = setInterval(tick, 1000);

function tick() {
    let now = new Date().getTime();
    console.log(now)
    let t = launchDate - now;
    console.log(t)
    if (t>0) {
        let days = Math.floor(t / (1000*60*60*24));
        if (days < 10) { days = "0" + days}
        let hours = Math.floor((t % (1000*60*60*24)) / (1000*60*60));
        if (hours < 10) { hours = "0" + hours}
        let mins = Math.floor((t % (1000*60*60*24)) / (1000*60));
        if (mins < 10) { mins = "0" + mins}
        let secs = Math.floor((t % (1000*60*60*24)) / (1000));
        if (secs < 10) { secs = "0" + secs}

        let time = `${days} : ${hours} : ${mins} : ${secs}`;
        console.log(time)
        document.querySelector('.countdown').innerText = time;
    }
}