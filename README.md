# Face Detection with DeepFace

Este projeto utiliza a biblioteca **DeepFace** para realizar reconhecimento facial em tempo real utilizando a webcam.

## Requisitos

Certifique-se de ter instalado os seguintes pacotes antes de executar o código:

```bash
pip install opencv-python deepface
```

## Como Executar

1. Coloque uma imagem de referência no diretório do código e nomeie-a como **`reference.jpg`**.
2. Execute o script 

## Funcionamento

- O código captura imagens da webcam em tempo real.
- A cada 30 quadros, ele verifica se a face detectada na câmera corresponde à imagem de referência.
- Se houver correspondência, exibe "MATCH!" na tela.
- Se não houver correspondência, exibe "NO MATCH!".
- Para encerrar a execução, pressione a tecla **Q**.

## Exemplo de Uso

- Para rodar corretamente, tenha certeza de que a imagem **`reference.jpg`** está no mesmo diretório do código.
- O modelo tentará verificar a similaridade entre a imagem capturada e a imagem de referência.

## Observações

- Caso o reconhecimento facial não funcione corretamente, verifique se a iluminação e o ângulo da câmera estão adequados.

