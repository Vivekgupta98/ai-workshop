# Workshop Glossary

| Term | Beginner definition |
| --- | --- |
| Agent | A system in which a model participates in a bounded loop that observes state and chooses or proposes the next action. |
| One-shot call | One input is sent to a model and one response is returned, without a loop. |
| State | The explicit data carried between graph nodes. |
| Node | One named unit of work that reads state and returns state updates. |
| Edge | A permitted transition from one node to another. |
| Router | Deterministic code that reads state and selects an edge. It should not make another model call. |
| Schema | A structured contract describing required fields and their types. |
| ReAct | A loop that records reasoning, evidence or observation, an action or fix, and whether another iteration is needed. |
| Tool | A narrowly defined capability an agent can request, such as executing code. |
| Guardrail | A limit or validation rule that constrains unsafe, expensive, or invalid behavior. |
| Trace | One complete recorded request through an application or agent. |
| Span | One recorded operation inside a trace, such as a model call or graph node. |
| Evaluation case | An input paired with expectations that make success assessable. |
| Oracle | The source used to decide the correct result, such as hidden tests or a reviewed reference solution. |
| LLM-as-judge | A model used to score interpreted qualities under a fixed rubric. It is an evaluator, not ground truth. |
| Handoff | Structured data passed from one agent role to another. |
| Durable execution | Execution whose recorded history allows work to continue after a process restart. |
| SSE | Server-Sent Events, a one-way HTTP stream used here for ordered progress updates. |
| Idempotency | The property that safely retrying the same operation does not create unintended duplicate effects. |
