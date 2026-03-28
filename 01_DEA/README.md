-----

# ☁️ 01\_DEA: AWS Certified Data Engineer - Associate

このリポジトリでは、AWSを用いたモダン・データエンジニアリングの実装と、DEA資格合格に向けた技術検証を記録します。

## 🎯 学習テーマ

  - **IaC (Infrastructure as Code)**: Terraformを用いた、再現可能かつ冪等なデータ基盤の自動構築。
  - **データ連携 (SDK)**: Python (boto3) を用いた、インフラ操作とデータレイクへのデータ投入・取得の自動化。
  - **データレイク構築**: S3を中心としたスケーラブルで疎結合なストレージ設計。
  - **データ品質保証 (Data Quality)**: 取得データに対する、プログラムベースの統計的バリデーションの実装。
  - **サーバーレス分析**: Glue/Athenaを活用した、スキーマ自動管理とSQLによるオンデマンド分析。

## 📂 構成 (Directory Structure)

- **infrastructure/**: TerraformによるAWSリソース（S3, Glue, IAM）の定義。
- **src/**: データ転送、バリデーション、バッチ処理用のPythonスクリプト。
- **docs/images/**: 構築および実行エビデンス（スクリーンショット）。

-----

## 🛠️ 実装プロジェクト: Modern Data Lake Pipeline

### 1\. プロジェクト概要

データエンジニアリングのベストプラクティスに基づき、インフラの自動化（Terraform）、データのパイプライン化（Boto3/Python）、そしてサーバーレス分析（Glue/Athena）を統合した基盤を構築しました。手動操作を完全に排除し、コードベースでデータレイクの全ライフサイクルを管理することを目標とします。

### 2\. 処理フロー (Mermaid)

```mermaid
sequenceDiagram
    participant PC as Local PC (VS Code)
    participant TF as Terraform (IaC)
    participant PY as Python (boto3)
    participant S3 as AWS S3 (Data Lake)
    participant Glue as AWS Glue (Catalog)
    participant Athena as Amazon Athena (Query)
    participant GH as GitHub (Repository)

    Note over PC, Athena: 1. インフラ構築 & データ投入フェーズ
    PC->>TF: terraform apply
    TF->>S3: S3バケット作成
    TF->>Glue: DB & クローラ作成
    PC->>PY: upload_csv_data.py
    PY->>S3: データのアップロード (csv_data/*.csv)
    
    # 修正箇所:定義済みのS3からTFへ矢印を向ける
    S3-->>TF: 作成完了

    Note over PC, Athena: 2. データ整理 & 分析フェーズ
    PC->>Glue: クローラ実行
    Glue->>S3: CSVをスキャン
    Glue->>Glue: メタデータ（スキーマ）を自動登録
    PC->>Athena: SELECTクエリ実行
    Athena->>Glue: スキーマを参照
    Athena->>S3: 生データを読み取り
    Athena-->>PC: 結果を表示

    Note over PC, GH: 3. 成果管理フェーズ
    PC->>GH: git push origin main
    Note right of GH: 実績をREADMEに集約
```

### 3\. 実行エビデンス (Sprint 1: S3 Foundation)

#### 🚀 インフラ構築とデータ投入

手動操作を一切排除し、構築から投入までを「コード」で完結させています。

| 項目 | エビデンス画像 |
| :--- | :--- |
| **Terraform Apply ログ** | ![Apply Log](01_DEA/infrastructure/docs/images/terraform_apply_log.png) |
| **アップロード成功ログ** | ![Upload Log](01_DEA/infrastructure/docs/images/uploadlog.png) |
| **AWSコンソール確認** | ![AWS Console](01_DEA/infrastructure/docs/images/aws-s3-console3.png) |
| **S3 Read & Validation** | ![S3 Read Success](01_DEA/infrastructure/docs/images/s3_read_success.png) |

#### 🔍 データの取得とバリデーション

取得したデータに対し、プログラムによる自動検証（品質保証）を実施したログです。

| 項目 | エビデンス画像 |
| :--- | :--- |
| **S3 Read & Validation** | ![S3 Read Success](01_DEA/infrastructure/docs/images/s3_read_success.png) |

> **Summary (Sprint 1)**:
> インフラの再現性（IaC）とデータの整合性（Validation）をコードで担保する基盤を確立しました。

-----

### 4\. 実行エビデンス (Sprint 2: Batch Processing)

#### 🚀 複数ファイルの一括スキャンとバリデーションのスケール

1つのファイル指定から、バケット内の全オブジェクトを自動検知して処理するスケーラブルなパイプラインへ進化させました。

| 項目 | エビデンス画像 |
| :--- | :--- |
| **S3コンソール (ファイル一覧)** | ![S3 Batch List](01_DEA/infrastructure/docs/images/s3_batch_list.png) |
| **一括スキャン実行ログ** | ![Batch Execution Log](01_DEA/infrastructure/docs/images/batch_execution_log.png) |

> **Summary (Sprint 2)**:
> `list_objects_v2` を活用し、データ量の増加に対応可能な検知ロジックを実装。特定のキーワードに基づく品質チェックを全件自動で実施できることを確認しました。

-----

### 5\. 実行エビデンス (Sprint 3: Modern Data Stack Integration)

#### 🚀 Glueによるカタログ化とAthenaでのサーバーレス分析

S3上の生データをAWS Glueで自動スキャン（Schema Discovery）し、Amazon Athenaを用いてSQLで分析するモダンなパイプラインを統合しました。

| 項目 | 内容 | エビデンス画像 |
| :--- | :--- | :--- |
| **Glue Schema Discovery** | CSVから `id`, `topic`, `status` を抽出 | ![Table Detail](01_DEA/infrastructure/docs/images/Table-Detail-AWS-Glue-Console.png) |
| **Athena SQL Query** | S3上のデータをSQLで直接抽出 | ![Athena Query](01_DEA/infrastructure/docs/images/Atena-consle.png) |
| **動的更新 (120%達成)** | インフラ変更なしで新規データ反映 | ![Athena Update](01_DEA/infrastructure/docs/images/image_2bf783.jpg) |

> **Summary (Sprint 3)**:
> 「スキーマ・オン・リード」を実現。データの構造をGlue Data Catalogで一元管理することで、S3を「クエリ可能なデータベース」として活用する、疎結合で強力な分析基盤を確立しました。データの追加に対して分析側が自動追従することを確認し、パイプラインの動的な連携を実証しました。

-----

> **Summary (Project Total)**:
> 本プロジェクトを通じて、AWSを用いたサーバーレス・データ分析基盤の設計・構築・運用に必要となる、IaC、SDK、ETL/カタログ管理、SQL分析の主要スキルを統合的に実証しました。

-----