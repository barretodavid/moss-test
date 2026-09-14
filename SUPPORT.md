# Timeout behavior

Timeouts are whole seconds. The allowed range is inclusive, from 1 to 60.
Values below 1 are clamped to 1; values above 60 are clamped to 60.
The support term for the lower bound is the one second floor.
