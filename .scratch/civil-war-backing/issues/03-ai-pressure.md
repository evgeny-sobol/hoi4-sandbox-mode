# 03 - AI pressure

Status: resolved
Type: task
Blocked by: 01

## What to build

A backer's AI is nudged toward the kin side with lend-lease desire, and
with volunteer desire where the engine rule already allows volunteers
(fascism, communism). No `can_send_volunteers` override is granted, so
democratic and neutrality backers stay materiel/diplomatic.

## Acceptance criteria

- [ ] Every backer carries an AI lend-lease desire toward the kin side.
- [ ] Fascism and communism backers carry a volunteer desire toward the kin
      side.
- [ ] Democratic and neutrality backers send no volunteers, by rule.
- [ ] Over an observer session, at least one backer is seen lending or
      volunteering to its kin side.

## Answer

add_ai_strategy(send_lend_lease_desire, kin, 200) for every backer; send_volunteers_desire only for fascism/communism backers. No can_send_volunteers override. Observer run clean.
