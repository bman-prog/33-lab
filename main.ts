let melody = ["E D C D", "E E E:8 R:8", "D D D", "E G G", "E D C D", "E E E:8 R:8", "D D D", "D C"]
for (let measure of melody) {
    music.playMelody(measure, 80)
}
