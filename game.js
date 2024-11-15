var Module = {
    totalDependencies: 0,
    preRun: [],
    postRun: [],
    
    // Handle the initialization of the game
    onRuntimeInitialized: function() {
        console.log("Game is ready!");
        startGame();
    },

    // Custom function to start the game
    startGame: function() {
        const canvas = document.getElementById("game-canvas");
        canvas.width = 800;
        canvas.height = 600;

        gameLoop();
    },

    // Game loop function to update the game and render each frame
    gameLoop: function() {
        // Call the Python code in the WebAssembly module to update and render
        Module._game_update();

        // Request the next frame
        requestAnimationFrame(Module.gameLoop);
    }
};

// Load the WebAssembly file (game.wasm)
function loadWASM() {
    var script = document.createElement('script');
    script.src = "game.js";
    script.onload = function() {
        Module.onRuntimeInitialized();
    };
    document.body.appendChild(script);
}

// Initialize the game on page load
window.onload = function() {
    loadWASM();
};
