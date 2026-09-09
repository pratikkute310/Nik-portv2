from fpdf import FPDF

OUT = "Nikita-Deshmukh-Resume.pdf"


class Resume(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Nikita Deshmukh  ·  Cloud & DevOps Engineer  ·  Pune, Maharashtra, India", align="C")

    def section(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(13, 122, 78)
        self.cell(0, 7, title.upper())
        self.ln(2)
        x, y = self.get_x(), self.get_y()
        self.set_draw_color(13, 122, 78)
        self.set_line_width(0.4)
        self.line(x, y, 200, y)
        self.ln(3)
        self.set_text_color(20, 20, 20)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.set_x(14)
        self.multi_cell(0, 4.4, "- " + text)


pdf = Resume(format="A4", unit="mm")
pdf.set_auto_page_break(auto=True, margin=16)
pdf.add_page()
pdf.set_margins(14, 14, 14)

pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(17, 20, 24)
pdf.cell(0, 9, "Nikita Deshmukh")
pdf.ln(8)
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(13, 122, 78)
pdf.cell(0, 6, "Cloud & DevOps Engineer")
pdf.ln(7)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(70, 70, 70)
pdf.multi_cell(
    0,
    4.5,
    "Pune, Maharashtra, India  |  deshmukhnikita2001@gmail.com\n"
    "linkedin.com/in/nikita-deshmukh-36ab25197  |  github.com/Nikita-Deshmukh",
)

pdf.section("Professional summary")
pdf.set_font("Helvetica", "", 9.5)
pdf.multi_cell(
    0,
    4.5,
    "Cloud & DevOps Engineer with 4+ years of experience designing, automating, and operating "
    "cloud-native platforms across AWS and Red Hat OpenShift. Skilled in Kubernetes, Terraform, "
    "Infrastructure as Code, CI/CD, Docker, observability, DevSecOps, AWS infrastructure, and "
    "PostgreSQL. Experienced in SRE practices and production incident response, with a strong "
    "focus on system reliability, GDPR-aligned security controls, cost optimization, and "
    "AI-driven operational automation.",
)

pdf.section("Experience")
pdf.set_font("Helvetica", "B", 10.5)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 5, "Software Engineer I  |  Volkswagen Group Digital Solutions India, Pune")
pdf.ln(5)
pdf.set_font("Helvetica", "I", 9)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 4.5, "Lastenheftassistant (LHA)  -  AI-Powered Requirements Engineering Tool  |  Aug 2022 - Present")
pdf.ln(6)
pdf.set_text_color(20, 20, 20)
for item in [
    "Designed and maintained Helm-based Kubernetes architecture for dev/test/staging/production with parameterized configs, dependency management, and zero-downtime releases.",
    "Built multi-stage Docker images for Python and Node.js with OpenShift-compliant security, non-root execution, and Docker Compose for local multi-container environments.",
    "Automated Aurora PostgreSQL schema migrations using Alembic and Kubernetes Jobs.",
    "Developed GitHub Actions CI/CD with SonarQube quality gates, Black Duck scanning, staging deployments, and production release approvals.",
    "Operated Prometheus, Grafana, Loki, Tempo, and OpenTelemetry for monitoring, logs, tracing, dashboards, and email alerts.",
    "Supported production incident triage and root-cause analysis using SRE practices.",
    "Managed TLS certificate lifecycle, secure routes, and Kubernetes secrets across OpenShift environments with GDPR-aligned data protection.",
    "Enforced outbound network security through custom proxy whitelist controls and domain-based egress restrictions.",
    "Reduced project costs by 35-40% through optimized pod configurations and pod creation strategy.",
    "Designed the LHA architecture migration path from OpenShift to an AWS-native solution (in progress).",
    "Built automated RCA workflows integrating LLMs to correlate infrastructure events, pod failures, deployments, and application logs.",
    "Collaborated in Agile Scrum using Jira across sprint planning, refinement, reviews, and retrospectives.",
]:
    pdf.bullet(item)

pdf.set_font("Helvetica", "B", 10.5)
pdf.ln(2)
pdf.cell(0, 5, "Core AWS Infrastructure & Platform Engineering")
pdf.ln(6)
for item in [
    "Launched EC2 in custom VPCs with security groups, EBS, key pairs, private subnets, internet gateways, NAT gateways, and NACLs.",
    "Set up Application Load Balancers and autoscaling groups across multiple availability zones.",
    "Managed S3 lifecycle and bucket policies; created IAM users, groups, and roles with least-privilege access.",
    "Created reusable Terraform modules to provision AWS infrastructure (EC2, VPC, S3).",
    "Deployed containerized applications on Amazon ECS using Docker images in ECR.",
    "Configured CloudWatch logs, alarms, and dashboards for performance tracking and incident response.",
    "Designed a compute-optimized AVA chatbot on AWS Lambda and ALB, reducing infrastructure costs by 60-70%.",
]:
    pdf.bullet(item)

pdf.set_font("Helvetica", "B", 10.5)
pdf.ln(2)
pdf.cell(0, 5, "Hackathon Projects")
pdf.ln(6)
pdf.bullet("Built an AI-powered assistant for automotive PFMEA risk rating (i.mobilithon 5.0).")
pdf.bullet("Developed an automated system for comparing automotive part specifications using Python and OpenCV (i.mobilithon 4.0).")

pdf.section("Skills")
pdf.set_font("Helvetica", "", 9.5)
pdf.multi_cell(
    0,
    4.5,
    "Cloud: AWS (EC2, S3, IAM, ECS), Azure (VNet, VMs, Key Vault), Red Hat OpenShift\n"
    "Containers: Docker, Kubernetes, EKS, Helm\n"
    "IaC & CI/CD: Terraform, YAML, GitHub Actions, Jenkins\n"
    "Observability: Grafana, Loki, Prometheus, Tempo, CloudWatch, SNS\n"
    "DevSecOps: SonarQube, Black Duck, Trivy, RBAC, IAM, OIDC, TLS/SSL, secrets management\n"
    "Data: PostgreSQL (Aurora RDS), DynamoDB, Alembic\n"
    "Automation: Python, Bash, Power Platform  |  AIOps: LLM, OpenAI, prompt engineering",
)

pdf.section("Education")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 5, "Bachelor of Engineering, Pune University  -  9.52 CGPA")
pdf.ln(5)
pdf.set_font("Helvetica", "", 9.5)
pdf.cell(0, 5, "Aug 2018 - May 2022")

pdf.section("Awards & training")
pdf.bullet("i.mobilithon 4.0 - Second Runner-up, Volkswagen Group Innovation Hackathon (Oct 2024 - Dec 2024).")
pdf.bullet("OpenShift with Kubernetes, VW Group internal training; on-site visit to Shanghai, China.")

pdf.section("Languages")
pdf.set_font("Helvetica", "", 9.5)
pdf.cell(0, 5, "English and German (A2)")

pdf.output(OUT)
print("wrote", OUT)
