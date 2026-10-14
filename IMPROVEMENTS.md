# Repository Improvement Opportunities

## Operational resilience for Lambdas
- Add request validation and clearer error handling for Lambda entrypoints like `prepare_wafr_review`, which currently assumes keys such as `analysis_id`, `analysis_submitter`, and `analysis_name` always exist in the event payload and DynamoDB item. Missing fields or empty DynamoDB responses would raise uncaught `KeyError`/`TypeError` before reaching the generic `except` block. Consider validating inputs, short-circuiting with informative 4xx responses, and adding retries or circuit breakers around Bedrock and DynamoDB calls.
- Centralize environment variable parsing (for example, convert retry/timeouts to integers and validate that critical IDs like `KNOWLEDGE_BASE_ID` and `LLM_MODEL_ID` are set) so Lambda code fails fast with actionable errors instead of surfacing downstream exceptions.

## CDK stack maintainability
- Deduplicate imports in `wafr_genai_accelerator_stack.py` and split stack configuration (e.g., optional feature toggles) into typed helper structures. The current stack file repeats imports such as `aws_stepfunctions`/`aws_stepfunctions_tasks` and mixes string flags for options, which makes drift and bugs more likely. A configuration dataclass or SSM-driven settings module would improve clarity.
- Separate high-level stack wiring from resource configuration details (for example, build smaller constructs for networking, Lambda packages, and Bedrock knowledge base setup). This would make it easier to test and evolve individual subsystems without touching the monolithic stack file.

## Observability and operations
- Standardize structured logging and metrics across services. For instance, `prepare_wafr_review` logs raw event payloads but does not emit metrics around DynamoDB fetch/update latency, Bedrock calls, or downstream workload creation. Introducing a common logging format and emitting CloudWatch metrics would help track performance and failure hotspots.
- Add integration and unit test coverage for Lambdas and Step Functions handlers. Even lightweight tests with `moto`/`localstack` and contract tests for payload schemas would prevent regressions as the accelerator evolves.

## Security hardening
- Review IAM policies and S3 bucket settings in the CDK stack to ensure least privilege and consistent encryption/SSL enforcement. Extract policy generation into helpers and add automated checks (such as `cdk-nag`) to catch overly broad permissions early in the pipeline.
- Validate and sanitize all user-supplied data before using it in workload creation or knowledge-base queries to reduce the risk of injection or privilege-escalation issues.
