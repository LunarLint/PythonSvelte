<script>
  import {
    Col,
    Container,
    Row,
    Button,
    Modal,
    ModalBody,
    ModalFooter,
    Spinner,
    Alert,
    Table,
  } from "sveltestrap";
  import Card from "sveltestrap/src/Card.svelte";
  import CardBody from "sveltestrap/src/CardBody.svelte";
  import CardHeader from "sveltestrap/src/CardHeader.svelte";
  import CardFooter from "sveltestrap/src/CardFooter.svelte";
  import { Input, Label } from "sveltestrap";

  let showResult = 0;
  let open = false;
  // const toggle = () => (open = !open);
  function toggle() {
    open = !open;
    showResult = 0;
  }

  let ele = {};
  function initEle() {
    ele = {
      OverallQual: "",
      YearBuilt: "",
      YearRemodAdd: "",
      TotalBsmtSF: "",
      GrLivArea: "",
      FullBath: "",
      GarageCars: "",
      MSZ_num: "",
      NbHd_num: "",
      ExtQ_num: "",
      BsQ_num: "",
      KiQ_num: "",
    };
  }

  function buildEle() {
    ele = {
      OverallQual: 5,
      YearBuilt: 1961,
      YearRemodAdd: 1961,
      TotalBsmtSF: 882,
      GrLivArea: 896,
      FullBath: 1,
      GarageCars: 1,
      MSZ_num: 2,
      NbHd_num: 1,
      ExtQ_num: 2,
      BsQ_num: 1,
      KiQ_num: 2,
    };
  }
  let buildJson;
  async function getPredict(ele) {
    // if(!ele.datetime||!ele.weather||!ele.temp||!ele.atemp||!ele.humidity){
    //     toggle()
    //     return
    // }
    buildJson = { ...ele };

    buildJson.OverallQual = buildJson.OverallQual;
    buildJson.YearBuilt = buildJson.YearBuilt;
    buildJson.YearRemodAdd = buildJson.YearRemodAdd;
    buildJson.TotalBsmtSF = buildJson.TotalBsmtSF;
    buildJson.GrLivArea = buildJson.GrLivArea;
    buildJson.FullBath = buildJson.FullBath;
    buildJson.GarageCars = buildJson.GarageCars;
    buildJson.MSZ_num = buildJson.MSZ_num;
    buildJson.NbHd_num = buildJson.NbHd_num;
    buildJson.ExtQ_num = buildJson.ExtQ_num;
    buildJson.BsQ_num = buildJson.BsQ_num;
    buildJson.KiQ_num = buildJson.KiQ_num;

    // console.log(buildJson);
    // console.log(buildJson.datetime.toLocaleString('ko-KR'))
    let { ...comJson } = buildJson;
    comJson = [comJson];
    const endpoint = "http://127.0.0.1:5000/predict";
    const res = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(comJson),
    });

    let result;
    if (res.ok) {
      result = await res.json();
      initEle();
      return result;
    } else {
      result = await res.text();
      throw new Error(result);
    }
  }

  let promise;

  async function handleClick(ele) {
    if (
      !ele.OverallQual ||
      !ele.YearBuilt ||
      !ele.YearRemodAdd ||
      !ele.TotalBsmtSF ||
      !ele.GrLivArea ||
      !ele.FullBath ||
      !ele.GarageCars ||
      !ele.MSZ_num ||
      !ele.NbHd_num ||
      !ele.ExtQ_num ||
      !ele.BsQ_num ||
      !ele.KiQ_num
    ) {
      toggle();
      return false;
    }
    showResult = 2;
    const wait = (timeToDelay) =>
      new Promise((resolve) => setTimeout(resolve, timeToDelay));
    await wait(1000 + Math.random() * 2000);
    showResult = 1;
    promise = getPredict(ele);
  }
</script>

<Container>
  <Row class="mt-4">
    <Col>
      <Card>
        <CardBody><h3 class="fw-bold">집값 예측</h3></CardBody>
      </Card>
    </Col>
  </Row>
  <!-- 날짜 날씨 온도 체감온도 습도 -->
  <Row class="mt-4">
    <Col>
      <Label for="OverallQual">전체 재료 및 마지막 품질</Label>
      <Input type="number" id="OverallQual" bind:value={ele.OverallQual} />
    </Col>
    <Col>
      <Label for="YearBuilt">최초 공사 연도</Label>
      <Input type="number" id="YearBuilt" bind:value={ele.YearBuilt} />
    </Col>
    <Col>
      <Label for="YearRemodAdd">리모델링 연도</Label>
      <Input type="number" id="YearRemodAdd" bind:value={ele.YearRemodAdd} />
    </Col>
    <Col>
      <Label for="TotalBsmtSF">지하 평수</Label>
      <Input type="number" id="TotalBsmtSF" bind:value={ele.TotalBsmtSF} />
    </Col>
    <Col>
      <Label for="GrLivArea">생활 면적</Label>
      <Input type="number" id="GrLivArea" bind:value={ele.GrLivArea} />
    </Col>
    <Col>
      <Label for="FullBath">욕실 수</Label>
      <Input type="number" id="FullBath" bind:value={ele.FullBath} />
    </Col>
  </Row>
  <Row class="mt-4">
    <Col>
      <Label for="GarageCars">차고 크기(차 대수)</Label>
      <Input type="number" id="GarageCars" bind:value={ele.GarageCars} />
    </Col>
    <Col>
      <Label for="MSZ_num">일반 면적 크기</Label>
      <Input type="number" id="MSZ_num" bind:value={ele.MSZ_num} />
    </Col>
    <Col>
      <Label for="NbHd_num">도시 경계 내의 물리적 위치</Label>
      <Input type="number" id="NbHd_num" bind:value={ele.NbHd_num} />
    </Col>
    <Col>
      <Label for="ExtQ_num">외부재료 품질</Label>
      <Input type="number" id="ExtQ_num" bind:value={ele.ExtQ_num} />
    </Col>
    <Col>
      <Label for="BsQ_num">지하실 높이</Label>
      <Input type="number" id="BsQ_num" bind:value={ele.BsQ_num} />
    </Col>
    <Col>
      <Label for="KiQ_num">주방품질</Label>
      <Input type="number" id="KiQ_num" bind:value={ele.KiQ_num} />
    </Col>
  </Row>
  <Row class="mt-3">
    <Col>
      <Button on:click={buildEle}>테스트 용</Button>
    </Col>
  </Row>
  <Row class="mt-3">
    <Col>
      <Button
        on:click={() => {
          handleClick(ele);
        }}>예측 하기</Button
      >
    </Col>
  </Row>
  <div>
    <Modal isOpen={open} {toggle}>
      <ModalBody>
        <h4>모두 다 입력해 주세요.</h4>
      </ModalBody>
      <ModalFooter>
        <Button color="secondary" on:click={toggle} size="sm">확인</Button>
      </ModalFooter>
    </Modal>
  </div>
  {#if showResult === 1}
    <Row class="mt-4 text-center">
      <Col>
        {#await promise}
          <Spinner color="secondary" />
          <h5>AI is Thinking.......</h5>
        {:then result}
          <Card>
            <CardHeader>
              <h4>AI가 예측 하였습니다.</h4>
            </CardHeader>
            <CardBody>
              <h1 class="text-bold">
                {result.prediction} 불
              </h1>
            </CardBody>
            <CardFooter class="small text-muted text-center">
              <Table style="width:50%;" class="text-muted m-auto" size="sm">
                <thead>
                  <tr>
                    <th scope="row">목록</th>
                    <th>전체 재료 및 마지막 품질</th>
                    <th>최초 공사연도</th>
                    <th>리모델링 연도</th>
                    <th>지하 평수</th>
                    <th>생활 면적</th>
                    <th>욕실</th>
                    <th>차고 크기(차 대수)</th>
                    <th>일반 면적 크기</th>
                    <th>도시 경계 내의 물리적 위치</th>
                    <th>외부재료 품질</th>
                    <th>지하실 높이</th>
                    <th>주방품질</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">값</th>
                    <td>{buildJson.OverallQual}</td>
                    <td>{buildJson.YearBuilt}</td>
                    <td>{buildJson.YearRemodAdd}</td>
                    <td>{buildJson.TotalBsmtSF}</td>
                    <td>{buildJson.GrLivArea}</td>
                    <td>{buildJson.FullBath}</td>
                    <td>{buildJson.GarageCars}</td>
                    <td>{buildJson.MSZ_num}</td>
                    <td>{buildJson.NbHd_num}</td>
                    <td>{buildJson.ExtQ_num}</td>
                    <td>{buildJson.BsQ_num}</td>
                    <td>{buildJson.KiQ_num}</td>
                  </tr>
                </tbody>
              </Table>
            </CardFooter>
          </Card>
        {:catch error}
          <Alert color="danger" fade={false}>
            <h4 class="alert-heading text-capitalize">
              죄송합니다.<br />
              현재 예측을 이용할 수 없습니다.<br />
              나중에 다시 시도해 주십시오.
            </h4>
            {error.message}
          </Alert>
        {/await}
      </Col>
    </Row>
  {:else if showResult === 2}
    <Row class="mt-4 text-center">
      <Col>
        <Spinner color="secondary" />
        <h5>AI is Thinking....</h5>
      </Col>
    </Row>
  {/if}
</Container>
