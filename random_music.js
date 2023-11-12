var musicSources = [
    'random_music/Lukrembo - Biscuit.mp3',
    'random_music/Palm Trees.mp3',
    'random_music/So Lucky - PYC.mp3',
    'random_music/Tofuus - Soda.mp3',
    'random_music/Tofuus - Magnolia jane.mp3',
    'random_music/Tofuus - Soda.mp3',
    'random_music/Tokyo Music Walker- Way Home.mp3',
    'random_music/Vein - KV.mp3',
];

// Function to play a random song
function random_bgMusic() {
    var randomIndex = Math.floor(Math.random() * musicSources.length);
    var audio = document.getElementById('bgMusic');
    audio.src = musicSources[randomIndex];
    audio.load();
    audio.play();
}
