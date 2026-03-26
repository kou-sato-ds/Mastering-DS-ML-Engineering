# ☁️ 01_DEA: AWS Certified Data Engineer - Associate

このセクションでは、AWSを用いたデータエンジニアリングの実装と、DEA資格合格に向けた技術検証を記録します。

## 🎯 学習テーマ
- **IaC (Infrastructure as Code)**: Terraformを用いたデータ基盤の自動構築。
- **データレイク構築**: S3を中心としたスケーラブルなストレージ設計。
- **データ統合**: AWS GlueによるETL処理とカタログ管理（予定）。
- **分析基盤**: Amazon Athenaを用いたサーバーレスなクエリ実行（予定）。

## 📂 構成 (Directory Structure)
- `infrastructure/`: TerraformによるAWSリソースの定義。
- `src/`: データ転送・加工用のPythonスクリプト。
- `images/`: 構築エビデンス（スクリーンショット）。

---

## 🛠️ 実装プロジェクト: S3 Data Lake Foundation

### 1. 概要
Terraformを使用して、データレイクの基盤となるS3バケットを自動構築しました。

### 2. 工夫した点
- **変数の分離**: `variables.tf` を活用し、バケット名やリージョンを柔軟に変更可能に設計。
- **Git管理の最適化**: 巨大なバイナリファイルや状態ファイルを `.gitignore` で適切に除外し、軽量なリポジトリを維持。

### 3. エビデンス
#### Terraformによるリソース構築
![Terraform Apply](infrastructure/docs/images/terraform-code.png)

#### AWSコンソールでの実体確認
![AWS Console](infrastructure/docs/images/aws-s3-console.png)

## 🛠️ Data Engineering: Infrastructure as Code (IaC)

### 01_DEA/infrastructure
AWSのデータレイク基盤をTerraformで構築・管理しています。

- **使用技術**: Terraform (v1.x), AWS (S3)
- **実施内容**: 
  - S3バケットの自動プロビジョニング
  - `.gitignore` によるステートファイル（機密情報）の厳格な管理
  - 変数（`variables.tf`）を利用した環境の柔軟な切り替え

#### 🚀 実行エビデンス
Terraformによって1秒でリソースが生成されることを確認済みです。

| Terraform Apply ログ | AWS コンソール確認 |
| :---: | :---: |
| ![Apply Log](infrastructure/docs/images/terraform_apply_log.png) | ![AWS Console](infrastructure/docs/images/aws_s3_console2.png) |

-----

# ☁️ 01\_DEA: AWS Certified Data Engineer - Associate

このセクションでは、AWSを用いたデータエンジニアリングの実装と、DEA資格合格に向けた技術検証を記録します。

## 🎯 学習テーマ

  - **IaC (Infrastructure as Code)**: Terraformを用いたデータ基盤の自動構築。
  - **データ連携 (SDK)**: Python (boto3) を用いたインフラ操作とデータ投入の自動化。
  - **データレイク構築**: S3を中心としたスケーラブルなストレージ設計。

## 📂 構成 (Directory Structure)

  - `infrastructure/`: TerraformによるAWSリソースの定義。
  - `src/`: データ転送・操作用のPythonスクリプト（boto3利用）。
  - `docs/images/`: 構築および実行エビデンス。

-----

## 🛠️ 実装プロジェクト: S3 Data Lake Foundation

### 1\. 概要

Terraformで構築したS3バケットに対し、Python (boto3) を用いてプログラム経由でデータを投入するパイプラインの基礎を構築しました。

### 2\. 処理フロー (Mermaid)

```mermaid
sequenceDiagram
    participant PC as Local PC (VS Code)
    participant TF as Terraform (IaC)
    participant PY as Python (boto3)
    participant AWS as AWS (S3 Bucket)
    participant GH as GitHub (Repository)

    Note over PC, AWS: 1. インフラ構築フェーズ
    PC->>TF: terraform apply
    TF->>AWS: S3バケット作成
    AWS-->>TF: 作成完了

    Note over PC, AWS: 2. データ連携フェーズ
    PC->>PY: python upload_test.py
    PY->>AWS: S3接続テスト & データ投入
    Note right of AWS: raw/hello-from-python.txt
    AWS-->>PY: アップロード成功 (Success)

    Note over PC, GH: 3. 成果管理フェーズ
    PC->>GH: git push origin main
    Note right of GH: 実績をREADMEに集約
```

### 3\. 実行エビデンス

#### 🚀 開発環境と実行ログ

VS Code上でのディレクトリ管理および、PythonスクリプトによるS3へのアップロード成功ログです。

| 項目 | エビデンス画像 |
| :--- | :--- |
| **ディレクトリ構成 (VS Code)** |![Apply Log](infrastructure\docs\images\vscode.png)|
| **アップロード成功ログ** |![Apply Log](infrastructure\docs\images\UploadLog.png)|

#### 🏗️ AWSコンソールでの実体確認

プログラム経由で作成されたフォルダおよびファイルが、クラウド上に正しく反映されていることを確認しました。

| 項目 | エビデンス画像 |
| :--- | :--- |
| **S3バケット内のオブジェクト一覧** |![Apply Log](infrastructure\docs\images\aws-s3-console3.png)|

> **Summary**: 手動操作を一切排除し、インフラ構築からデータ投入までを「コード」で完結させました。