<script>
  import {
    Container,
    Styles,
    TabContent,
    TabPane,
    Row,
    Col,
    Badge,
  } from "sveltestrap";
  import Card from "sveltestrap/src/Card.svelte";
  import HousePredict from "./lib/HousePredict.svelte";
</script>

<Styles />

<Container>
  <HousePredict />
</Container>
