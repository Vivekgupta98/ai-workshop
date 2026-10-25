# Local Judge0

Days 3 to 5 execute code through Judge0 CE in Docker. The API is bound to `127.0.0.1:2358`; the workshop does not use RapidAPI or a hosted Judge0 service.

The Compose file comes from the official Judge0 CE `v1.13.1` release archive:

```text
https://github.com/judge0/judge0/releases/download/v1.13.1/judge0-v1.13.1.zip
SHA-256: d83f002c98f2c3935fc4fec3abcb863191e7c863ffcd202401d03a8f7e1fa513
```

## Start and test

From the workshop root:

```bash
./workshop judge0-start
./workshop judge0-test
```

The startup command creates `judge0/judge0.conf` with random local database passwords. Git ignores this generated file.

The smoke test compiles and runs:

- Python 3.8.1;
- C++14 with GCC 9.2 and `-std=c++14`;
- Java 11.

Judge0 1.13.1 contains an OpenJDK 11 runtime but not a Java 11 compiler. The startup script configures language ID 27 to compile with the bundled Java 13 compiler using `--release 11`, then execute with OpenJDK 11. This checks Java 11 syntax, APIs, bytecode, and runtime behavior without downloading another JDK.

## Other commands

```bash
./workshop judge0-logs
./workshop judge0-stop
./workshop doctor --start-judge0
```

## Platform note

Judge0 CE `v1.13.1` is tested on Linux, and its release instructions recommend Ubuntu 22.04 with cgroups v1. Docker Desktop may behave differently on macOS and Windows. Use Linux or WSL 2 if the privileged worker cannot run correctly.

The server and worker use privileged containers because the official image relies on `isolate`. Run the stack only on a trusted development machine and never expose port 2358 publicly.
