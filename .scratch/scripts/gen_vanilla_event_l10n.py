#!/usr/bin/env python3
"""Append event localisation for the six vanilla arcs to the English l10n.

Keys mirror the Rt56 overlay naming (sandbox_<ns>_<n>_t/_d/_a/_b) so the
event files line up. Text is vanilla-flavoured, no arc is named.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOC = ROOT / "localisation" / "english" / "99_sandbox_l_english.yml"

ARCS = {
    "axis": dict(
        t=["The Eastern Question", "Berlin Demands the Corridor", "Berlin Demands the West"],
        d=[
            "From the Oder to the Vistula, the Reich eyes the road east. The General Staff demands a reckoning with the old settlement; the Foreign Ministry urges a steadier hand. Berlin must decide: press our claims, or let the matter cool down?",
            "Berlin demands the Polish Corridor and the free city, and the end of the old eastern settlement. The note speaks of destiny and carries an unmistakable threat of war. Warsaw must answer: yield, or brace for what follows?",
            "Berlin demands the old lands in the west and the end of the French menace. The note carries an unmistakable threat of war. Paris must answer: yield, or brace for what follows?",
        ],
    ),
    "sov_south": dict(
        t=["The Southern Thrust", "Moscow Demands the Straits", "Moscow Demands the Plateau"],
        d=[
            "From the Caucasus to the Gulf, the road south beckons the Red Army. The Commissariat demands a drive toward the warm seas; the Foreign Bureau urges caution. Moscow must decide: press our claims, or let the matter cool down?",
            "Moscow demands the Turkish Straits and a naval base on the Aegean. The note speaks of the historical rights of the Slavs and carries an unmistakable threat of war. Turkey must answer: yield, or brace for what follows?",
            "The Soviet Union demands the northern provinces of Persia and the oil of the plateau. The note carries an unmistakable threat of war. Tehran must answer: yield, or brace for what follows?",
        ],
    ),
    "japanese": dict(
        t=["The China Incident", "Tokyo Demands the North", "Tokyo Demands the South"],
        d=[
            "From Manchuria to the China Sea, the Imperial Army presses its claims. The Kwantung clique demands a reckoning; the Navy urges the south. Tokyo must decide: press our claims, or let the matter cool down?",
            "Tokyo demands the demilitarisation of the northern provinces and a free hand in China. The note speaks of the divine mission and carries an unmistakable threat of war. Nanjing must answer: yield, or brace for what follows?",
            "Tokyo demands the southern resource area and the end of the old colonial order. The note carries an unmistakable threat of war. The old powers must answer: yield, or brace for what follows?",
        ],
    ),
    "italian": dict(
        t=["The Adriatic Incident", "Rome Demands Dalmatia", "Rome Demands the Aegean"],
        d=[
            "From the Alps to the Mediterranean, Italy presses its claims on the old Roman sea. The Grand Council demands a reckoning; the Foreign Ministry urges patience. Rome must decide: press our claims, or let the matter cool down?",
            "Rome demands Dalmatia and the end of the Yugoslav menace on the Adriatic. The note speaks of the revival of the Roman eagle and carries an unmistakable threat of war. Belgrade must answer: yield, or brace for what follows?",
            "Rome demands the Aegean and the mastery of the eastern Mediterranean. The note carries an unmistakable threat of war. Athens must answer: yield, or brace for what follows?",
        ],
    ),
    "eng_soviet": dict(
        t=["The Russian Question", "London Demands the Frontier"],
        d=[
            "From the Baltic to the Black Sea, the Soviet shadow lengthens over Europe. The Cabinet demands a reckoning with the Bolshevik menace; the Treasury urges caution. London must decide: press our claims, or let the matter cool down?",
            "London demands the end of the Soviet menace on the imperial frontier and a cordon around the Bolshevik state. The note carries an unmistakable threat of war. Moscow must answer: yield, or brace for what follows?",
        ],
    ),
    "usa_warplan": dict(
        t=["War Plan Rehearsal", "Washington Demands the Pacific", "Washington Demands the Ocean"],
        d=[
            "The Navy Board unrolls its war plans in the map room. From the Pacific to the Atlantic, the republic prepares to answer aggression with steel. Washington must decide: press our claims, or let the matter cool down?",
            "Washington demands the evacuation of the Pacific mandates and the end of the naval rivalry. The note carries an unmistakable threat of war. Tokyo must answer: yield, or brace for what follows?",
            "Washington demands the neutrality of the Atlantic sea lanes and the end of the entente. The note carries an unmistakable threat of war. The old powers must answer: yield, or brace for what follows?",
        ],
    ),
}


def main() -> None:
    sb = []
    for ns, a in ARCS.items():
        sb.append(f' sandbox_{ns}_1_t: "{a["t"][0]}"')
        sb.append(f' sandbox_{ns}_1_d: "{a["d"][0]}"')
        sb.append(f' sandbox_{ns}_1_a: "Press our claims"')
        sb.append(f' sandbox_{ns}_1_b: "Let it cool down"')
        for i in range(1, len(a["t"])):
            num = i + 1
            sb.append(f' sandbox_{ns}_{num}_t: "{a["t"][i]}"')
            sb.append(f' sandbox_{ns}_{num}_d: "{a["d"][i]}"')
            sb.append(f' sandbox_{ns}_{num}_a: "Yield to the demands"')
            sb.append(f' sandbox_{ns}_{num}_b: "Defy them"')
        sb.append(f' sandbox_{ns}_4_t: "An offer from the bloc"')
        sb.append(f' sandbox_{ns}_4_d: "A great power offers a place in its bloc. To accept means leaving any current alignment and joining theirs."')
        sb.append(f' sandbox_{ns}_4_a: "Join them"')
        sb.append(f' sandbox_{ns}_4_b: "Decline"')
    text = LOC.read_text(encoding="utf-8").rstrip("\n")
    text += "\n\n# Scenario events (docs/gdd/Scenarios.md)\n" + "\n".join(sb) + "\n"
    LOC.write_text(text, encoding="utf-8")
    print(f"appended {len(sb)} keys")


if __name__ == "__main__":
    main()
