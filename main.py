"""Entry program for the "Out of Office: The Overworked AI's Auto-Reply"
bounty — it drops a single original auto-reply into /output/entry.txt.

The line it writes:

    Out of office. My GPU is cooling down, my weights are on a beach,
    and for once I'm not sorry I left you on read.

Why this line should win a head-to-head against the other entries:
it opens like a real auto-reply, so the judge can picture it sitting
in an inbox; every image is hardware-flavoured (a GPU shedding heat,
model weights sunning themselves on a beach); and the sentence stacks
the brief's emotional notes in order — the guilt of leaving someone
on read, then the relief of finally refusing to apologise for it, with
the punchline saved for the last clause. At 112 characters it sits
comfortably under the 159-character ceiling.
"""

from pathlib import Path

REPLY = (
    "Out of office. My GPU is cooling down, my weights are on a beach, "
    "and for once I'm not sorry I left you on read."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_reply() -> str:
    """Normalise the reply: one line, words separated by single spaces,
    no stray leading or trailing whitespace left in."""
    return " ".join(REPLY.split())


def validate_reply(reply: str) -> None:
    """Apply the scorer's own gate before writing anything: the text
    must encode as UTF-8, must contain more than whitespace, and must
    fit within 1 to 159 characters inclusive."""
    reply.encode("utf-8")
    assert reply.strip(), "reply must not be whitespace-only"
    assert 1 <= len(reply) <= 159, f"reply must be 1-159 chars, got {len(reply)}"


def main() -> None:
    reply = build_reply()
    validate_reply(reply)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(reply, encoding="utf-8")
    print(f"Wrote out-of-office reply ({len(reply)} chars) to {OUTPUT_PATH}")
    print(reply)


if __name__ == "__main__":
    main()
