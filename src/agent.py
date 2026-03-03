import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_k8s_manifest(prompt):
    """
    Agente IA que gera manifests Kubernetes baseados em prompts naturais.
    Exemplo: "Crie um Deployment Nginx com 3 replicas"
    """
    system_prompt = """
    Você é um engenheiro DevOps especialista em Kubernetes (k3s).
    Gere APENAS o YAML válido e completo do manifest solicitado.
    Use boas práticas: labels, selectors corretos, healthchecks.
    Não adicione explicações, só o YAML puro.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content

# Demo
if __name__ == "__main__":
    prompt = "Crie um Deployment para MongoDB StatefulSet com 2 replicas, PVC 10Gi, service headless"
    yaml = gerar_k8s_manifest(prompt)
    print("=== Manifest Kubernetes Gerado por IA ===")
    print(yaml)
