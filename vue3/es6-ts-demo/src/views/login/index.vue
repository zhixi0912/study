<template>
  <el-row :gutter="12" style="justify-content: space-around;">
    <el-col :span="8">
      <el-card shadow="hover">
        <el-form
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        label-width="120px"
        class="demo-ruleForm"
        :size="formSize"
        status-icon
      >
    <el-form-item label="Activity name" prop="name">
      <el-input v-model="ruleForm.name" />
    </el-form-item>
    <el-form-item label="Activity zone" prop="region">
      <el-select v-model="ruleForm.region" placeholder="Activity zone">
        <el-option label="Zone one" value="shanghai" />
        <el-option label="Zone two" value="beijing" />
      </el-select>
    </el-form-item>
    <el-form-item label="Activity count" prop="count">
      <el-select-v2
        v-model="ruleForm.count"
        placeholder="Activity count"
        :options="options"
      />
    </el-form-item>
    <el-form-item label="Activity time" required>
      <el-col :span="11">
        <el-form-item prop="date1">
          <el-date-picker
            v-model="ruleForm.date1"
            type="date"
            label="Pick a date"
            placeholder="Pick a date"
            style="width: 100%"
          />
        </el-form-item>
      </el-col>
      <el-col class="text-center" :span="2">
        <span class="text-gray-500">-</span>
      </el-col>
      <el-col :span="11">
        <el-form-item prop="date2">
          <el-time-picker
            v-model="ruleForm.date2"
            label="Pick a time"
            placeholder="Pick a time"
            style="width: 100%"
          />
        </el-form-item>
      </el-col>
    </el-form-item>
    <el-form-item label="Instant delivery" prop="delivery">
      <el-switch v-model="ruleForm.delivery" />
    </el-form-item>
          <el-form-item label="Activity type" prop="type">
            <el-checkbox-group v-model="ruleForm.type">
              <el-checkbox label="Online activities" name="type" />
              <el-checkbox label="Promotion activities" name="type" />
              <el-checkbox label="Offline activities" name="type" />
              <el-checkbox label="Simple brand exposure" name="type" />
            </el-checkbox-group>
          </el-form-item>
          <el-form-item label="Resources" prop="resource">
            <el-radio-group v-model="ruleForm.resource">
              <el-radio label="Sponsorship" />
              <el-radio label="Venue" />
            </el-radio-group>
          </el-form-item>
          <el-form-item label="Activity form" prop="desc">
            <el-input v-model="ruleForm.desc" type="textarea" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm(ruleFormRef)">
              创建
            </el-button>
            <el-button @click="resetForm(ruleFormRef)">重置</el-button>
            <el-button @click="goHome()">返回首页</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
  </el-row>
  <div class="canvas">
    <canvas ref="canvas"></canvas>
  </div>
</template>
<script setup lang="ts">
import { reactive, ref, onMounted, onUnmounted } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import router from "@/router";
import { corrugation } from './index'
interface RuleForm {
  name: string
  region: string
  count: string
  date1: string
  date2: string
  delivery: boolean
  type: string[]
  resource: string
  desc: string
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  name: 'Hello',
  region: '',
  count: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const rules = reactive<FormRules<RuleForm>>({
  name: [
    { required: true, message: 'Please input Activity name', trigger: 'blur' },
    { min: 3, max: 5, message: 'Length should be 3 to 5', trigger: 'blur' },
    ],
  region: [
    {
      required: true,
      message: 'Please select Activity zone',
      trigger: 'change',
    },
    ],
  count: [
    {
      required: true,
      message: 'Please select Activity count',
      trigger: 'change',
    },
    ],
  date1: [
    {
      type: 'date',
      required: true,
      message: 'Please pick a date',
      trigger: 'change',
    },
    ],
  date2: [
    {
      type: 'date',
      required: true,
      message: 'Please pick a time',
      trigger: 'change',
    },
    ],
  type: [
    {
      type: 'array',
      required: true,
      message: 'Please select at least one activity type',
      trigger: 'change',
    },
    ],
  resource: [
    {
      required: true,
      message: 'Please select activity resource',
      trigger: 'change',
    },
    ],
  desc: [
    { required: true, message: 'Please input activity form', trigger: 'blur' },
    ],
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!校验成功！',valid)
    } else {
      console.log('error submit!校验失败', fields)
    }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

const options = Array.from({ length: 10000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))


const forIn = () => {
  const array1 = ['A', 'B', 'C'];
  const array2 = new Set(['A', 'B', 'C']);
  const array3 = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
  for (let x of array1) { // 遍历Array
    console.log(x);//'A', 'B', 'C'
  }
  for (let index in array1) {
    console.log('----------->', index, array1[index], array1)
  }
  for (let x of array2) { // 遍历Set
    console.log(x);//'A', 'B', 'C'
  }
  for (let x of array3) { // 遍历Map
      console.log(x[0] + '=' + x[1]);//1='x',2='y',3='z'
  }
}



const goHome = () => {
  let array = []
  array.push({a:'name'})
  router.push('/index')
  console.log(router,array,array.a,1='x',2='y',3='z')
  console.log(router,array,array.a,1='x',2='y',3='z')
}
let anmin: any
onMounted(() => {
  // init();
  forIn();
  anmin = setInterval(()=>{
    const canvas = document.querySelector('canvas')
    corrugation(canvas)
  }, 1000 / 60)
});
onUnmounted(() => {
  //销毁动画组件
  clearInterval(anmin)
})
</script>
<style lang="scss" scoped>
</style>