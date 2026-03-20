# API-Example-Doc-Test Mapping Matrix (Initial)

This is the initial baseline for Step 7 in pyorbbecsdk.

| Capability | API | Example | Doc | Auto Test | Notes |
|---|---|---|---|---|---|
| Context creation and query devices | Yes | Yes | Yes | Partial | test/test_context.py depends on hardware today. |
| Device info and sensor list | Yes | Yes | Yes | Partial | test/test_device.py depends on hardware. |
| Pipeline create and camera param | Yes | Yes | Yes | Partial | test/test_pipeline.py depends on hardware. |
| Recording and playback | Yes | Yes | Yes | No | Needs playback no-hardware test path with bag input. |
| IMU and multi-stream | Yes | Yes | Yes | No | Example coverage exists; no CI assertions yet. |
| Point cloud and post-processing | Yes | Yes | Yes | No | Example coverage exists; no CI assertions yet. |
| Network device and force IP | Yes | Yes | Yes | No | Hardware/network environment required. |

## Gap List (P0/P1/P2)

### P0

- Split current hardware-coupled tests into no-hardware and hardware markers so PR Gate can run stable checks.
- Add smoke tests for module import, object construction, and basic API availability without device dependency.

### P1

- Add playback-based no-hardware regression test using bag data where feasible.
- Add example-level assertions for key scripts (quick_start, playback, record_no_gui).

### P2

- Expand to full function-level mapping from docs and generated API stubs.
- Auto-generate matrix rows from examples and test files to keep mapping updated.
