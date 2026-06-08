# Khi bắt đầu một dự án mới:
- Thiết kế kiến trúc.
- Tiêu chuẩn & quy trình.
- Phân công rõ ràng.
- Giám sát & kiểm soát.

# Quy trình phát triển phần mềm:
V-model:
```mermaid
flowchart TB
    A[User Requirements] --> B[System Requirements]
    B --> C[Architecture Design]
    C --> D[Module / Detail Design]
    D --> E[Coding / Implementation]

    E --> F[Unit Testing]
    F --> G[Integration Testing]
    G --> H[System Testing]
    H --> I[Acceptance Testing]

    A -. validates .-> I
    B -. verifies .-> H
    C -. verifies .-> G
    D -. verifies .-> F

# BIG PICTURE WORKFLOW:
1. BrainStorm:
 - Ý tưởng như cầu.
 - Nhu cầu.
 - Brainstorm.
 - Xác định mục tiêu.
2. SPECS:
 - Domains.
 - Features.
 - User Roles.
 - API Contracts.
 - Business Rule.
3. Architecture (ADR):
 - ADRs.
 - Tech stack.
 - Architecture.
 - Rules & Conventions.
 - Folder structure.
4. Planning (Sprint/task):
 - Backlog.
 - Sprints.
 - User Stories.
 - Tasks (lớn).
 - Ưu tiên & ước lượng.
5. Parallel Excution (Team + AI):
 - Mỗi thành viên + AI.
 - Chọn task trong sprint.
 - Làm song song.
 - Commit thường xuyên.
6. Review & Merge:
 - PR/ Review.
 - Verify (human/AI).
 - Resolve conflict.
 - Merge vào main.
7. Next Sprint (Lặp lại):
 - Retro.
 - Cải tiến.
 - Sprint tiếp theo.

**BONUS:** Mọi hoạt động đều dựa trên context chung: SPECS + ADRs + Contracts + Rules.

# Ý nghĩa các thư mục chính:
1. /specs: Nơi chứa các đặc tả nghiệp vụ, domain, tính năng, API contracts, ...
2. /adrs: Ghi lại các quyết định kiến trúc, công nghệ, quy ước, nguyên tắc.
3. /Planning: Kế hoạch sản phẩm, backlog, sprint plan, timeline, ...
4. /tasks: Danh sách user stories/ tasks theo sprint, trạng thái, owner, ...
5. /src: Codebase của dự án.
6. /docs: Tài liệu hướng dẫn, runbook, how-to, architecture diagrams, ...

# Nguyên tắc và lưu ý quan trọng để team + AI làm việc hiệu quả:
**flow:** context đúng -> AI hiểu đúng -> Code đúng -> Sản phẩm đúng.
1. SPEC-DRIVEN (Không code trước):
 - Làm rõ "cái gì", "tại sao", "như thế nào" trước khi code.
 - Specs là nguồn sự thật chung cho cả team + AI.
 **Spec tốt = ít đổi hướng = ít tốn chi phí.**
2. ADR là nền (Không mạnh AI nào một kiểu):
 - Mọi quyết định kiến trúc, công nghệ, quy tắc... đều ghi lại.
 - Thay đổi phải có ADR mới.
 **ADR giúp team thống nhất và dễ dàng scale.**
3. Task đủ lớn (AI tự chia nhỏ task):
 - Team chỉ quản lý task lớn (feature level).
 - AI có không gian để tự lập plan và chia subtask.
 **Đừng chia quá nhỏ, hãy để AI tự phát huy.**
4. Làm việc qua contract (Không phụ thuộc ngầm):
 - Giao tiếp giữa các domain/service qua contract (API/Proto/Events).
 - Team chỉ cần biết "cam kết", Không cần biết cách làm.
 **Contract rõ ràng = tách rời tốt = làm song song hiệu quả.**
5. AI luôn đọc context trước khi code:
 - Agent phải đọc đầy đủ context base trước khi bắt đầu.
 - Cập nhật context là trách nhiệm của cả team.
 **Context càng rõ ràng AI càng làm đúng.**
6. Git WorkFlow là kỷ luật:
 - Branch rõ ràng.
 - PR + review là bắt buộc.
 - Mọi thay đổi đều có lịch sử đề truy vết.
 **Kỷ luật Git = an toàn = dễ tác động.**

**BONUS:** Context base luôn phải được duy trì.
1. Specs cập nhật khi có thay đổi.
2. ADR luôn là mới nhất.
3. Contract/docs luôn đúng.
4. Tasks & plan luôn cập nhập trạng thái.
5. Agents.md luôn rõ ràng.

# Một vài tip and trick:
## ADR TỐT GIÚP TEAM + AI LÀM VIỆC HIỆU QUẢ
1. ADR: Text Driven/ Test Strategy:
 - Quyết định team ưu tiên viết test hoặc acceptance criteria rõ ràng trước khi implementation.
 - Lý do thân thiện với AI:
  + Agent có đích đến rõ ràng.
  + Agent có thể tự code -> tự chạy test -> tự sửa chữa.
  + Review dễ hơn vì nhìn vào test pass/fail.
  **Câu chốt:** Test là hợp đồng hành vi của hệ thống.
2. ADR: Domain Split (Microservice/ Hybrid):
 - Quyết định: Chia hệ thống theo domain rõ ràng và Có thể Microservice hoặc Modular Monolith (Hybrid).
 - Vì sao thân thiện với AI:
  + Mỗi member phụ trách một domain -> Làm song song dễ hơn.
  + Giảm phụ thuộc, ít conflict code.
  + Agent chỉ cần context của service/module đó -> giảm "over-context".
  **Câu chốt:** Chia domain tốt = chia context tốt.
3. ADR: API Contract First:
 - Quyết định: Các service giao tiếp qua contract rõ ràng trước khi code.
 - Lợi ích: 
  + Service A không cần đọc sâu code của Service B.
  + Frontend, Backend, Agent có thể làm song song.
  + Khi contract thay đổi -> Phải review rõ ràng.
  **Câu chốt:** Team scale bằng contract, không scale bằng hiểu ngầm.
4. ADR: Project Structure & Coding Convention:
 - Quyết định: Thống nhất cấu trúc dự án, quy ước code và kỹ thuật.
 - Vì sao quan trọng với AI:
  + Agent không tự sáng tạo mỗi lần một kiểu.
  + Code sinh ra đồng nhất hơn.
  + Review, bảo trì, refactor dễ dàng hơn.
  **Câu chốt:** Không có convention, AI sẽ nhân bản sự hỗn loạn rất nhanh.
5. Definition Of Done (DOD):
 - Quyết định: Một task chỉ được đóng khi đáp ứng đầy đủ:
  + Code đã Implement.
  + Test pass (unit, integration/e2e).
  + Docs/ Contracts cập nhật (nếu có).
  + No lint error.
  + PR reviewed & approved.
  + Task status cập nhật (Done).
 - Lợi ích với Team + AI:
  + Agent biết khi nào dừng.
  + Member biết khi nào được merge.
  + Tránh tình trạng "Code xong rồi nhưng chưa xong thật".
 **Câu chốt:** Done không phải là code chạy được. Done là đủ chuẩn để merge.

**ADR tốt = Context đủ - Boundary rõ ràng - Contract rõ ràng - Test rõ - Team + AI làm việc song song, chất lượng cao và bền vững.**